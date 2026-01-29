import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class OtpVerificationScreenWithRegistration extends StatefulWidget {
  final String email;
  final String name;
  final String password;

  const OtpVerificationScreenWithRegistration({
    Key? key,
    required this.email,
    required this.name,
    required this.password,
  }) : super(key: key);

  @override
  State<OtpVerificationScreenWithRegistration> createState() =>
      _OtpVerificationScreenWithRegistrationState();
}

class _OtpVerificationScreenWithRegistrationState
    extends State<OtpVerificationScreenWithRegistration> {
  final TextEditingController otpController = TextEditingController();
  bool isLoading = false;
  String? errorMessage;
  int resendCount = 0;
  int timerSeconds = 0;

  final String baseUrl = 'http://127.0.0.1:8000';

  @override
  void initState() {
    super.initState();
    startTimer();
  }

  void startTimer() {
    timerSeconds = 60;
    Future.delayed(const Duration(seconds: 1), () {
      if (mounted && timerSeconds > 0) {
        setState(() {
          timerSeconds--;
        });
        startTimer();
      }
    });
  }

  Future<void> verifyOTPAndRegister() async {
    final otp = otpController.text.trim();

    if (otp.isEmpty || otp.length != 6) {
      setState(() {
        errorMessage = 'Please enter a 6-digit OTP';
      });
      return;
    }

    setState(() {
      isLoading = true;
      errorMessage = null;
    });

    try {
      final verifyResponse = await http.post(
        Uri.parse('$baseUrl/api/auth/verify-otp/'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'email': widget.email,
          'otp_code': otp,
        }),
      );

      if (verifyResponse.statusCode != 200) {
        final data = json.decode(verifyResponse.body);
        setState(() {
          errorMessage = data['message'] ?? 'Invalid OTP';
          isLoading = false;
        });
        return;
      }

      final registerResponse = await http.post(
        Uri.parse('$baseUrl/api/users/create/'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'name': widget.name,
          'emailid': widget.email,
          'password': widget.password,
        }),
      );

      if (registerResponse.statusCode == 201) {
        final loginResponse = await http.post(
          Uri.parse('$baseUrl/api/users/login/'),
          headers: {'Content-Type': 'application/json'},
          body: json.encode({
            'emailid': widget.email,
            'password': widget.password,
          }),
        );

        if (loginResponse.statusCode == 200) {
          final data = json.decode(loginResponse.body);
          if (mounted) {
            Navigator.pushReplacementNamed(
              context,
              '/user-profile',
              arguments: {
                'userId': data['user']['id'],
                'userName': data['user']['name'],
              },
            );
          }
        } else {
          setState(() {
            errorMessage = 'Registration completed. Please login.';
            isLoading = false;
          });
        }
      } else {
        final data = json.decode(registerResponse.body);
        setState(() {
          errorMessage = data['message'] ?? 'Registration failed';
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = 'Error: ${e.toString()}';
        isLoading = false;
      });
    }
  }

  Future<void> resendOTP() async {
    if (resendCount >= 3) {
      setState(() {
        errorMessage = 'Maximum resend attempts exceeded.';
      });
      return;
    }

    setState(() {
      isLoading = true;
      errorMessage = null;
    });

    try {
      final response = await http.post(
        Uri.parse('$baseUrl/api/auth/resend-otp/'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'email': widget.email}),
      );

      if (response.statusCode == 200) {
        setState(() {
          resendCount++;
          isLoading = false;
          timerSeconds = 60;
          otpController.clear();
        });
        startTimer();
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('OTP resent. Check terminal.'),
            backgroundColor: Colors.green,
          ),
        );
      } else {
        final data = json.decode(response.body);
        setState(() {
          errorMessage = data['message'] ?? 'Failed to resend OTP';
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = 'Error: ${e.toString()}';
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Verify OTP'),
        backgroundColor: Colors.deepPurple,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              const SizedBox(height: 40),
              const Icon(Icons.lock_outline, size: 80, color: Colors.deepPurple),
              const SizedBox(height: 24),
              const Text('Verify OTP',
                  style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
              const SizedBox(height: 8),
              Text(
                'Enter the 6-digit OTP shown in terminal\n${widget.email}',
                style: const TextStyle(fontSize: 14, color: Colors.grey),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 32),
              TextField(
                controller: otpController,
                keyboardType: TextInputType.number,
                maxLength: 6,
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold, letterSpacing: 8),
                decoration: InputDecoration(
                  hintText: '000000',
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: const BorderSide(color: Colors.deepPurple, width: 2),
                  ),
                  counterText: '',
                ),
              ),
              const SizedBox(height: 16),
              if (errorMessage != null)
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: Colors.red.shade50,
                    border: Border.all(color: Colors.red),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Row(
                    children: [
                      const Icon(Icons.error_outline, color: Colors.red),
                      const SizedBox(width: 12),
                      Expanded(child: Text(errorMessage!, style: const TextStyle(color: Colors.red))),
                    ],
                  ),
                ),
              const SizedBox(height: 24),
              SizedBox(
                width: double.infinity,
                height: 50,
                child: ElevatedButton(
                  onPressed: isLoading ? null : verifyOTPAndRegister,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.deepPurple,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  child: isLoading
                      ? const SizedBox(
                          height: 20,
                          width: 20,
                          child: CircularProgressIndicator(strokeWidth: 2, valueColor: AlwaysStoppedAnimation<Color>(Colors.white)),
                        )
                      : const Text('Verify & Continue',
                          style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white)),
                ),
              ),
              const SizedBox(height: 16),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text("Didn't receive OTP? "),
                  GestureDetector(
                    onTap: timerSeconds > 0 || resendCount >= 3 ? null : resendOTP,
                    child: Text(
                      timerSeconds > 0
                          ? 'Resend in ${timerSeconds}s'
                          : resendCount >= 3
                              ? 'Max attempts reached'
                              : 'Resend OTP',
                      style: TextStyle(
                        color: timerSeconds > 0 || resendCount >= 3 ? Colors.grey : Colors.deepPurple,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              Text('Resend attempts: $resendCount/3',
                  style: const TextStyle(fontSize: 12, color: Colors.grey)),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    otpController.dispose();
    super.dispose();
  }
}
