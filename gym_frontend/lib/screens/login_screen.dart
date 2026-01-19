import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _obscurePassword = true;
  bool _isLoading = false;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  Future<void> _handleLogin() async {
    final email = _emailController.text.trim();
    final password = _passwordController.text.trim();

    if (email.isEmpty || password.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please enter email and password'),
          backgroundColor: Colors.red,
        ),
      );
      return;
    }

    setState(() {
      _isLoading = true;
    });

    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:8000/api/users/login/'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'emailid': email,
          'password': password,
        }),
      );

      setState(() {
        _isLoading = false;
      });

      final data = json.decode(response.body);

      if (response.statusCode == 200 && data['success'] == true) {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text(data['message'] ?? 'Login successful'),
              backgroundColor: Colors.green,
            ),
          );
          
          // Check user role and route accordingly
          final userRole = data['user']['role'];
          final userId = data['user']['id'];
          final userName = data['user']['name'];
          
          if (userRole == 'admin') {
            Navigator.pushReplacementNamed(context, '/admin-dashboard');
          } else if (userRole == 'trainer') {
            // Redirect to trainer dashboard
            final trainerId = data['user']['trainer_id'];
            Navigator.pushReplacementNamed(
              context,
              '/trainer-dashboard',
              arguments: {
                'trainerId': trainerId,
                'trainerName': userName,
              },
            );
          } else {
            // Check if user has a profile
            await _checkUserProfile(userId, userName);
          }
        }
      } else {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text(data['message'] ?? 'Login failed'),
              backgroundColor: Colors.red,
            ),
          );
        }
      }
    } catch (e) {
      setState(() {
        _isLoading = false;
      });
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Network error: $e'),
            backgroundColor: Colors.red,
          ),
        );
      }
    }
  }

  Future<void> _checkUserProfile(int userId, String userName) async {
    try {
      print('Checking profile for userId: $userId');
      final response = await http.get(
        Uri.parse('http://127.0.0.1:8000/api/profile/$userId/'),
      );

      print('Profile check response status: ${response.statusCode}');
      print('Profile check response body: ${response.body}');

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        print('Decoded data: $data');
        
        if (data['success'] == true) {
          // Profile exists
          final profile = data['profile'];
          print('Profile found: $profile');
          print('Payment status: ${profile['payment_status']}');
          
          if (profile['payment_status'] == true) {
            // Payment completed, go to home
            print('Navigating to /home');
            Navigator.pushReplacementNamed(
              context,
              '/home',
              arguments: {
                'userId': userId,
                'userName': userName,
              },
            );
          } else {
            // Payment not completed, go to payment screen
            print('Navigating to /payment with amount: ${profile['payment_amount']}, months: ${profile['target_months']}');
            Navigator.pushReplacementNamed(
              context,
              '/payment',
              arguments: {
                'userId': userId,
                'amount': profile['payment_amount'],
                'months': profile['target_months'],
                'userName': userName,
              },
            );
          }
        } else {
          // Profile not found, go to profile screen
          print('Profile not found, navigating to /user-profile');
          Navigator.pushReplacementNamed(
            context,
            '/user-profile',
            arguments: {
              'userId': userId,
              'userName': userName,
            },
          );
        }
      } else {
        // Profile not found, go to profile screen
        print('Profile not found (non-200 status), navigating to /user-profile');
        Navigator.pushReplacementNamed(
          context,
          '/user-profile',
          arguments: {
            'userId': userId,
            'userName': userName,
          },
        );
      }
    } catch (e) {
      // On error, go to profile screen
      Navigator.pushReplacementNamed(
        context,
        '/user-profile',
        arguments: {
          'userId': userId,
          'userName': userName,
        },
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: SingleChildScrollView(
          child: Column(
            children: [
              // Header with image
              Container(
                height: 200,
                width: double.infinity,
                decoration: const BoxDecoration(
                  image: DecorationImage(
                    image: NetworkImage(
                      'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800',
                    ),
                    fit: BoxFit.cover,
                  ),
                ),
                child: Container(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Colors.black.withOpacity(0.3),
                        Colors.black.withOpacity(0.6),
                      ],
                    ),
                  ),
                  padding: const EdgeInsets.all(20),
                  alignment: Alignment.centerLeft,
                  child: const Text(
                    'Fitness Gym',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 32,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
              // Login Form
              Padding(
                padding: const EdgeInsets.all(30.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'Login',
                      style: TextStyle(
                        fontSize: 28,
                        fontWeight: FontWeight.bold,
                        color: Colors.black,
                      ),
                    ),
                    const SizedBox(height: 10),
                    Text(
                      'Enter your registered email id or contact number and password to login into your account.',
                      style: TextStyle(
                        fontSize: 13,
                        color: Colors.grey[600],
                      ),
                    ),
                    const SizedBox(height: 30),
                    // Email Field
                    TextField(
                      controller: _emailController,
                      decoration: InputDecoration(
                        labelText: 'Email',
                        labelStyle: const TextStyle(
                          color: Color(0xFF7B4EFF),
                          fontSize: 14,
                        ),
                        suffixIcon: const Icon(
                          Icons.email_outlined,
                          color: Colors.grey,
                          size: 20,
                        ),
                        enabledBorder: const UnderlineInputBorder(
                          borderSide: BorderSide(color: Colors.grey),
                        ),
                        focusedBorder: const UnderlineInputBorder(
                          borderSide: BorderSide(color: Color(0xFF7B4EFF)),
                        ),
                      ),
                    ),
                    const SizedBox(height: 20),
                    // Password Field
                    TextField(
                      controller: _passwordController,
                      obscureText: _obscurePassword,
                      decoration: InputDecoration(
                        labelText: 'Password',
                        labelStyle: const TextStyle(
                          color: Color(0xFF7B4EFF),
                          fontSize: 14,
                        ),
                        suffixIcon: IconButton(
                          icon: Icon(
                            _obscurePassword
                                ? Icons.lock_outline
                                : Icons.lock_open_outlined,
                            color: Colors.grey,
                            size: 20,
                          ),
                          onPressed: () {
                            setState(() {
                              _obscurePassword = !_obscurePassword;
                            });
                          },
                        ),
                        enabledBorder: const UnderlineInputBorder(
                          borderSide: BorderSide(color: Colors.grey),
                        ),
                        focusedBorder: const UnderlineInputBorder(
                          borderSide: BorderSide(color: Color(0xFF7B4EFF)),
                        ),
                      ),
                    ),
                    const SizedBox(height: 10),
                    // Forgot Password
                    Align(
                      alignment: Alignment.centerRight,
                      child: TextButton(
                        onPressed: () {},
                        child: const Text(
                          'Forgot Password?',
                          style: TextStyle(
                            color: Colors.black,
                            fontSize: 12,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(height: 20),
                    // Login Button
                    SizedBox(
                      width: double.infinity,
                      height: 50,
                      child: ElevatedButton(
                        onPressed: _isLoading ? null : _handleLogin,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: const Color(0xFF7B4EFF),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(8),
                          ),
                          elevation: 0,
                        ),
                        child: _isLoading
                            ? const SizedBox(
                                height: 20,
                                width: 20,
                                child: CircularProgressIndicator(
                                  color: Colors.white,
                                  strokeWidth: 2,
                                ),
                              )
                            : const Text(
                                'LOGIN',
                                style: TextStyle(
                                  color: Colors.white,
                                  fontSize: 16,
                                  fontWeight: FontWeight.bold,
                                  letterSpacing: 1,
                                ),
                              ),
                      ),
                    ),
                    const SizedBox(height: 30),
                    // OR Divider
                    Row(
                      children: [
                        Expanded(
                          child: Divider(
                            color: Colors.grey[300],
                            thickness: 1,
                          ),
                        ),
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 15),
                          child: Text(
                            'OR',
                            style: TextStyle(
                              color: Colors.grey[600],
                              fontSize: 12,
                            ),
                          ),
                        ),
                        Expanded(
                          child: Divider(
                            color: Colors.grey[300],
                            thickness: 1,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 25),
                    // Social Login Buttons
                    Row(
                      children: [
                        Expanded(
                          child: OutlinedButton.icon(
                            onPressed: () {},
                            icon: const FaIcon(
                              FontAwesomeIcons.facebookF,
                              size: 18,
                              color: Color(0xFF1877F2),
                            ),
                            label: const Text(
                              'Facebook',
                              style: TextStyle(
                                color: Colors.black87,
                                fontSize: 14,
                              ),
                            ),
                            style: OutlinedButton.styleFrom(
                              padding: const EdgeInsets.symmetric(vertical: 12),
                              side: BorderSide(color: Colors.grey[300]!),
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(8),
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 15),
                        Expanded(
                          child: OutlinedButton.icon(
                            onPressed: () {},
                            icon: const FaIcon(
                              FontAwesomeIcons.google,
                              size: 18,
                              color: Color(0xFFDB4437),
                            ),
                            label: const Text(
                              'Google',
                              style: TextStyle(
                                color: Colors.black87,
                                fontSize: 14,
                              ),
                            ),
                            style: OutlinedButton.styleFrom(
                              padding: const EdgeInsets.symmetric(vertical: 12),
                              side: BorderSide(color: Colors.grey[300]!),
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(8),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 30),
                    // Register Link
                    Center(
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const Text(
                            "Don't have an account? ",
                            style: TextStyle(
                              color: Colors.black87,
                              fontSize: 14,
                            ),
                          ),
                          GestureDetector(
                            onTap: () {
                              Navigator.pushNamed(context, '/register');
                            },
                            child: const Text(
                              'Register',
                              style: TextStyle(
                                color: Color(0xFFFF6B35),
                                fontSize: 14,
                                fontWeight: FontWeight.bold,
                                decoration: TextDecoration.underline,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
