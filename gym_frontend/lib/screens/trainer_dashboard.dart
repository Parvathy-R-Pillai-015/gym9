import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

class TrainerDashboard extends StatefulWidget {
  final int trainerId;
  final String trainerName;

  const TrainerDashboard({
    super.key,
    required this.trainerId,
    required this.trainerName,
  });

  @override
  State<TrainerDashboard> createState() => _TrainerDashboardState();
}

class _TrainerDashboardState extends State<TrainerDashboard> {
  List<Map<String, dynamic>> _assignedUsers = [];
  List<Map<String, dynamic>> _pendingAttendance = [];
  List<Map<String, dynamic>> _reviews = [];
  double _averageRating = 0.0;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Future<void> _loadData() async {
    setState(() => _isLoading = true);
    await Future.wait([
      _loadAssignedUsers(),
      _loadPendingAttendance(),
      _loadReviews(),
    ]);
    setState(() => _isLoading = false);
  }

  Future<void> _loadAssignedUsers() async {
    try {
      final response = await http.get(
        Uri.parse(
          'http://127.0.0.1:8000/api/trainer/${widget.trainerId}/users/',
        ),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          setState(() {
            _assignedUsers = List<Map<String, dynamic>>.from(data['users']);
          });
        }
      }
    } catch (e) {
      print('Error loading assigned users: $e');
    }
  }

  Future<void> _loadPendingAttendance() async {
    try {
      final response = await http.get(
        Uri.parse(
          'http://127.0.0.1:8000/api/trainer/${widget.trainerId}/attendance/pending/',
        ),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          setState(() {
            _pendingAttendance = List<Map<String, dynamic>>.from(
              data['requests'],
            );
          });
        }
      }
    } catch (e) {
      print('Error loading pending attendance: $e');
    }
  }

  Future<void> _loadReviews() async {
    try {
      final response = await http.get(
        Uri.parse(
          'http://127.0.0.1:8000/api/reviews/trainer/${widget.trainerId}/',
        ),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          setState(() {
            _reviews = List<Map<String, dynamic>>.from(data['reviews']);
            _averageRating = data['average_rating'].toDouble();
          });
        }
      }
    } catch (e) {
      print('Error loading reviews: $e');
    }
  }

  Future<void> _acceptAttendance(int attendanceId, String userName) async {
    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:8000/api/attendance/accept/'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'attendance_id': attendanceId,
          'status': 'accepted',
        }),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text('Attendance accepted for $userName'),
              backgroundColor: Colors.green,
            ),
          );
          _loadData();
        }
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Error accepting attendance: $e'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  Future<void> _viewUserAttendance(int userId, String userName) async {
    try {
      final response = await http.get(
        Uri.parse('http://127.0.0.1:8000/api/attendance/user/$userId/'),
      );

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['success']) {
          _showAttendanceDialog(
            userName,
            List<Map<String, dynamic>>.from(data['attendances']),
            data['total_accepted'],
            data['total_pending'],
          );
        }
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('Error loading attendance: $e'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  void _showAttendanceDialog(
    String userName,
    List<Map<String, dynamic>> attendances,
    int totalAccepted,
    int totalPending,
  ) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('$userName - Attendance'),
        content: SizedBox(
          width: double.maxFinite,
          height: 400,
          child: Column(
            children: [
              Card(
                color: const Color(0xFF7B4EFF).withOpacity(0.1),
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      Column(
                        children: [
                          Text(
                            '$totalAccepted',
                            style: const TextStyle(
                              fontSize: 24,
                              fontWeight: FontWeight.bold,
                              color: Color(0xFF7B4EFF),
                            ),
                          ),
                          const Text('Total Accepted'),
                        ],
                      ),
                      Column(
                        children: [
                          Text(
                            '$totalPending',
                            style: const TextStyle(
                              fontSize: 24,
                              fontWeight: FontWeight.bold,
                              color: Colors.orange,
                            ),
                          ),
                          const Text('Pending'),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 16),
              Expanded(
                child: ListView.builder(
                  itemCount: attendances.length,
                  itemBuilder: (context, index) {
                    final att = attendances[index];
                    return ListTile(
                      leading: Icon(
                        att['status'] == 'accepted'
                            ? Icons.check_circle
                            : att['status'] == 'pending'
                            ? Icons.pending
                            : Icons.cancel,
                        color: att['status'] == 'accepted'
                            ? Colors.green
                            : att['status'] == 'pending'
                            ? Colors.orange
                            : Colors.red,
                      ),
                      title: Text(att['date']),
                      subtitle: Text('Status: ${att['status']}'),
                      trailing: att['accepted_date'] != null
                          ? Text(
                              'Accepted: ${att['accepted_date']}',
                              style: const TextStyle(fontSize: 10),
                            )
                          : null,
                    );
                  },
                ),
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Close'),
          ),
        ],
      ),
    );
  }

  void _showUserDetails(Map<String, dynamic> user) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(user['name']),
        content: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              _buildDetailRow('Email', user['email']),
              _buildDetailRow('Mobile', user['mobile']),
              _buildDetailRow('Age', '${user['age']} years'),
              _buildDetailRow('Gender', user['gender']),
              _buildDetailRow('Current Weight', '${user['current_weight']} kg'),
              _buildDetailRow('Current Height', '${user['current_height']} cm'),
              _buildDetailRow('Goal', user['goal']),
              _buildDetailRow('Target Weight', '${user['target_weight']} kg'),
              _buildDetailRow(
                'Target Months',
                '${user['target_months']} months',
              ),
              _buildDetailRow('Workout Time', user['workout_time']),
              _buildDetailRow('Diet Preference', user['diet_preference']),
              if (user['food_allergies'] != '')
                _buildDetailRow('Food Allergies', user['food_allergies']),
              if (user['health_conditions'] != '')
                _buildDetailRow('Health Conditions', user['health_conditions']),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Close'),
          ),
        ],
      ),
    );
  }

  void _createDietPlan(Map<String, dynamic> user) async {
    // Calculate target calories
    final calcResponse = await http.get(
      Uri.parse('http://127.0.0.1:8000/api/diet/calculate/${user['id']}/'),
    );

    if (calcResponse.statusCode != 200) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Failed to calculate calories'),
          backgroundColor: Colors.red,
        ),
      );
      return;
    }

    final calcData = json.decode(calcResponse.body);
    final targetCalories = calcData['target_calories'];
    final goal = calcData['goal'];
    final allergies = calcData['food_allergies'];

    // Get diet templates
    final templatesResponse = await http.get(
      Uri.parse(
        'http://127.0.0.1:8000/api/diet/templates/?goal=$goal&target_calories=$targetCalories',
      ),
    );

    if (templatesResponse.statusCode != 200) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Failed to load templates'),
          backgroundColor: Colors.red,
        ),
      );
      return;
    }

    final templatesData = json.decode(templatesResponse.body);
    final templates = List<Map<String, dynamic>>.from(templatesData['templates']);

    if (templates.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('No templates found for $goal goal'),
          backgroundColor: Colors.orange,
        ),
      );
      return;
    }

    // Show diet plan creation dialog
    showDialog(
      context: context,
      builder: (context) => _DietPlanDialog(
        userId: user['id'],
        userName: user['name'],
        trainerId: widget.trainerId,
        targetCalories: targetCalories,
        goal: goal,
        allergies: allergies,
        templates: templates,
      ),
    );
  }

  Widget _buildDetailRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 140,
            child: Text(
              '$label:',
              style: const TextStyle(fontWeight: FontWeight.bold),
            ),
          ),
          Expanded(child: Text(value)),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Trainer Dashboard - ${widget.trainerName}'),
        backgroundColor: const Color(0xFF7B4EFF),
        foregroundColor: Colors.white,
        actions: [
          IconButton(icon: const Icon(Icons.refresh), onPressed: _loadData),
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () {
              Navigator.pushReplacementNamed(context, '/login');
            },
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : SingleChildScrollView(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Pending Attendance Requests
                  if (_pendingAttendance.isNotEmpty) ...[
                    Card(
                      color: Colors.orange.shade50,
                      child: Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                const Icon(
                                  Icons.pending_actions,
                                  color: Colors.orange,
                                ),
                                const SizedBox(width: 8),
                                Text(
                                  'Pending Attendance Requests (${_pendingAttendance.length})',
                                  style: const TextStyle(
                                    fontSize: 18,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 12),
                            ListView.builder(
                              shrinkWrap: true,
                              physics: const NeverScrollableScrollPhysics(),
                              itemCount: _pendingAttendance.length,
                              itemBuilder: (context, index) {
                                final request = _pendingAttendance[index];
                                return Card(
                                  child: ListTile(
                                    leading: const CircleAvatar(
                                      child: Icon(Icons.person),
                                    ),
                                    title: Text(request['user_name']),
                                    subtitle: Text('Date: ${request['date']}'),
                                    trailing: ElevatedButton.icon(
                                      onPressed: () => _acceptAttendance(
                                        request['id'],
                                        request['user_name'],
                                      ),
                                      icon: const Icon(Icons.check),
                                      label: const Text('Accept'),
                                      style: ElevatedButton.styleFrom(
                                        backgroundColor: Colors.green,
                                        foregroundColor: Colors.white,
                                      ),
                                    ),
                                  ),
                                );
                              },
                            ),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(height: 20),
                  ],

                  // Assigned Users
                  Text(
                    'My Users (${_assignedUsers.length})',
                    style: const TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 16),
                  if (_assignedUsers.isEmpty)
                    const Center(
                      child: Padding(
                        padding: EdgeInsets.all(32.0),
                        child: Text(
                          'No users assigned yet',
                          style: TextStyle(fontSize: 16, color: Colors.grey),
                        ),
                      ),
                    )
                  else
                    ListView.builder(
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      itemCount: _assignedUsers.length,
                      itemBuilder: (context, index) {
                        final user = _assignedUsers[index];
                        return Card(
                          elevation: 4,
                          margin: const EdgeInsets.only(bottom: 12),
                          child: Padding(
                            padding: const EdgeInsets.all(16.0),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Row(
                                  children: [
                                    CircleAvatar(
                                      backgroundColor: const Color(0xFF7B4EFF),
                                      child: Text(
                                        user['name'][0].toUpperCase(),
                                        style: const TextStyle(
                                          color: Colors.white,
                                        ),
                                      ),
                                    ),
                                    const SizedBox(width: 12),
                                    Expanded(
                                      child: Column(
                                        crossAxisAlignment:
                                            CrossAxisAlignment.start,
                                        children: [
                                          Text(
                                            user['name'],
                                            style: const TextStyle(
                                              fontSize: 18,
                                              fontWeight: FontWeight.bold,
                                            ),
                                          ),
                                          Text(
                                            user['email'],
                                            style: const TextStyle(
                                              color: Colors.grey,
                                              fontSize: 12,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ),
                                    Container(
                                      padding: const EdgeInsets.symmetric(
                                        horizontal: 12,
                                        vertical: 6,
                                      ),
                                      decoration: BoxDecoration(
                                        color: user['remaining_days'] > 30
                                            ? Colors.green
                                            : user['remaining_days'] > 7
                                            ? Colors.orange
                                            : Colors.red,
                                        borderRadius: BorderRadius.circular(20),
                                      ),
                                      child: Text(
                                        '${user['remaining_days']} days left',
                                        style: const TextStyle(
                                          color: Colors.white,
                                          fontWeight: FontWeight.bold,
                                          fontSize: 12,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 12),
                                Row(
                                  mainAxisAlignment:
                                      MainAxisAlignment.spaceAround,
                                  children: [
                                    _buildInfoChip(
                                      Icons.fitness_center,
                                      'Goal',
                                      user['goal'],
                                    ),
                                    _buildInfoChip(
                                      Icons.calendar_today,
                                      'Plan',
                                      '${user['target_months']} months',
                                    ),
                                    _buildInfoChip(
                                      Icons.check_circle,
                                      'Attendance',
                                      '${user['total_attendance']}',
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 12),
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.end,
                                  children: [
                                    TextButton.icon(
                                      onPressed: () => _showUserDetails(user),
                                      icon: const Icon(Icons.info_outline),
                                      label: const Text('View Details'),
                                    ),
                                    const SizedBox(width: 8),
                                    ElevatedButton.icon(
                                      onPressed: () => _viewUserAttendance(
                                        user['id'],
                                        user['name'],
                                      ),
                                      icon: const Icon(Icons.calendar_month),
                                      label: const Text('Attendance'),
                                      style: ElevatedButton.styleFrom(
                                        backgroundColor: const Color(
                                          0xFF7B4EFF,
                                        ),
                                        foregroundColor: Colors.white,
                                      ),
                                    ),
                                    const SizedBox(width: 8),
                                    ElevatedButton.icon(
                                      onPressed: () => _createDietPlan(user),
                                      icon: const Icon(Icons.restaurant_menu),
                                      label: const Text('Diet Plan'),
                                      style: ElevatedButton.styleFrom(
                                        backgroundColor: Colors.green,
                                        foregroundColor: Colors.white,
                                      ),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                          ),
                        );
                      },
                    ),

                  // Reviews Section
                  const SizedBox(height: 24),
                  Card(
                    color: Colors.pink.shade50,
                    elevation: 4,
                    child: Padding(
                      padding: const EdgeInsets.all(16.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Row(
                                children: [
                                  const Icon(
                                    Icons.star,
                                    color: Colors.amber,
                                    size: 28,
                                  ),
                                  const SizedBox(width: 8),
                                  const Text(
                                    'User Reviews',
                                    style: TextStyle(
                                      fontSize: 20,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                ],
                              ),
                              if (_reviews.isNotEmpty)
                                Container(
                                  padding: const EdgeInsets.symmetric(
                                    horizontal: 12,
                                    vertical: 6,
                                  ),
                                  decoration: BoxDecoration(
                                    color: Colors.amber,
                                    borderRadius: BorderRadius.circular(20),
                                  ),
                                  child: Row(
                                    children: [
                                      Text(
                                        _averageRating.toStringAsFixed(1),
                                        style: const TextStyle(
                                          fontSize: 16,
                                          fontWeight: FontWeight.bold,
                                          color: Colors.white,
                                        ),
                                      ),
                                      const Icon(
                                        Icons.star,
                                        color: Colors.white,
                                        size: 16,
                                      ),
                                    ],
                                  ),
                                ),
                            ],
                          ),
                          const SizedBox(height: 16),
                          if (_reviews.isEmpty)
                            const Center(
                              child: Padding(
                                padding: EdgeInsets.all(20.0),
                                child: Text(
                                  'No reviews yet',
                                  style: TextStyle(color: Colors.grey),
                                ),
                              ),
                            )
                          else
                            ListView.builder(
                              shrinkWrap: true,
                              physics: const NeverScrollableScrollPhysics(),
                              itemCount: _reviews.length,
                              itemBuilder: (context, index) {
                                final review = _reviews[index];
                                return Card(
                                  margin: const EdgeInsets.only(bottom: 12),
                                  child: Padding(
                                    padding: const EdgeInsets.all(12.0),
                                    child: Column(
                                      crossAxisAlignment:
                                          CrossAxisAlignment.start,
                                      children: [
                                        Row(
                                          mainAxisAlignment:
                                              MainAxisAlignment.spaceBetween,
                                          children: [
                                            Row(
                                              children: [
                                                CircleAvatar(
                                                  radius: 16,
                                                  backgroundColor: Colors.blue,
                                                  child: Text(
                                                    review['user_name'][0]
                                                        .toUpperCase(),
                                                    style: const TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 14,
                                                    ),
                                                  ),
                                                ),
                                                const SizedBox(width: 8),
                                                Text(
                                                  review['user_name'],
                                                  style: const TextStyle(
                                                    fontWeight: FontWeight.bold,
                                                    fontSize: 14,
                                                  ),
                                                ),
                                              ],
                                            ),
                                            Row(
                                              children: [
                                                ...List.generate(5, (i) {
                                                  return Icon(
                                                    i < review['rating']
                                                        ? Icons.star
                                                        : Icons.star_border,
                                                    color: Colors.amber,
                                                    size: 18,
                                                  );
                                                }),
                                              ],
                                            ),
                                          ],
                                        ),
                                        const SizedBox(height: 8),
                                        Text(
                                          review['review_text'],
                                          style: const TextStyle(fontSize: 13),
                                        ),
                                        const SizedBox(height: 4),
                                        Text(
                                          review['created_at'],
                                          style: const TextStyle(
                                            fontSize: 11,
                                            color: Colors.grey,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                );
                              },
                            ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
    );
  }

  Widget _buildInfoChip(IconData icon, String label, String value) {
    return Column(
      children: [
        Icon(icon, size: 20, color: const Color(0xFF7B4EFF)),
        const SizedBox(height: 4),
        Text(label, style: const TextStyle(fontSize: 10, color: Colors.grey)),
        Text(
          value,
          style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold),
        ),
      ],
    );
  }
}

class _DietPlanDialog extends StatefulWidget {
  final int userId;
  final String userName;
  final int trainerId;
  final int targetCalories;
  final String goal;
  final String allergies;
  final List<Map<String, dynamic>> templates;

  const _DietPlanDialog({
    required this.userId,
    required this.userName,
    required this.trainerId,
    required this.targetCalories,
    required this.goal,
    required this.allergies,
    required this.templates,
  });

  @override
  State<_DietPlanDialog> createState() => _DietPlanDialogState();
}

class _DietPlanDialogState extends State<_DietPlanDialog> {
  int? _selectedTemplateIndex;
  final TextEditingController _notesController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text('Create Diet Plan - ${widget.userName}'),
      content: SizedBox(
        width: 600,
        height: 500,
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: Colors.green.shade50,
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'User Info',
                      style: const TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 16,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text('Goal: ${widget.goal.replaceAll('_', ' ').toUpperCase()}'),
                    Text('Target Calories: ${widget.targetCalories} cal/day'),
                    if (widget.allergies != 'none')
                      Text(
                        'Food Allergies: ${widget.allergies}',
                        style: const TextStyle(color: Colors.red),
                      ),
                  ],
                ),
              ),
              const SizedBox(height: 16),
              const Text(
                'Select Diet Plan Template:',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
              ),
              const SizedBox(height: 12),
              ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: widget.templates.length,
                itemBuilder: (context, index) {
                  final template = widget.templates[index];
                  final isSelected = _selectedTemplateIndex == index;
                  return Card(
                    color: isSelected ? Colors.green.shade100 : Colors.white,
                    margin: const EdgeInsets.only(bottom: 12),
                    child: InkWell(
                      onTap: () {
                        setState(() {
                          _selectedTemplateIndex = index;
                        });
                      },
                      child: Padding(
                        padding: const EdgeInsets.all(12),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                Icon(
                                  isSelected
                                      ? Icons.check_circle
                                      : Icons.circle_outlined,
                                  color: isSelected ? Colors.green : Colors.grey,
                                ),
                                const SizedBox(width: 8),
                                Expanded(
                                  child: Text(
                                    template['name'],
                                    style: TextStyle(
                                      fontWeight: FontWeight.bold,
                                      fontSize: 14,
                                      color: isSelected
                                          ? Colors.green.shade900
                                          : Colors.black,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 4),
                            Text(
                              template['description'],
                              style: const TextStyle(fontSize: 12),
                            ),
                            const SizedBox(height: 8),
                            if (isSelected) ...[
                              const Divider(),
                              const Text(
                                'Meal Plan Preview:',
                                style: TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 12,
                                ),
                              ),
                              const SizedBox(height: 4),
                              _buildMealPreview(template['meals_data']),
                            ],
                          ],
                        ),
                      ),
                    ),
                  );
                },
              ),
              const SizedBox(height: 16),
              TextField(
                controller: _notesController,
                maxLines: 3,
                decoration: InputDecoration(
                  labelText: 'Trainer Notes (Optional)',
                  hintText: 'Add any special instructions or notes...',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(8),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.pop(context),
          child: const Text('Cancel'),
        ),
        ElevatedButton(
          onPressed: _selectedTemplateIndex != null
              ? () => _saveDietPlan()
              : null,
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.green,
            foregroundColor: Colors.white,
          ),
          child: const Text('Create Diet Plan'),
        ),
      ],
    );
  }

  Widget _buildMealPreview(Map<String, dynamic> mealsData) {
    // Check if it's 7-day format (has monday, tuesday, etc keys)
    if (mealsData.containsKey('monday')) {
      // Show Monday's plan as sample
      final mondayMeals = mealsData['monday'] as Map<String, dynamic>;
      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            'Sample: Monday\'s Plan',
            style: TextStyle(
              fontSize: 11,
              fontStyle: FontStyle.italic,
              color: Colors.grey,
            ),
          ),
          const SizedBox(height: 4),
          _buildMealSection('Breakfast', mondayMeals['breakfast']),
          _buildMealSection('Lunch', mondayMeals['lunch']),
          _buildMealSection('Dinner', mondayMeals['dinner']),
          _buildMealSection('Snacks', mondayMeals['snacks']),
          const SizedBox(height: 4),
          const Text(
            '7-day plan with variety for each day',
            style: TextStyle(
              fontSize: 10,
              fontStyle: FontStyle.italic,
              color: Colors.green,
            ),
          ),
        ],
      );
    } else {
      // Old format: direct meals
      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          _buildMealSection('Breakfast', mealsData['breakfast']),
          _buildMealSection('Lunch', mealsData['lunch']),
          _buildMealSection('Dinner', mealsData['dinner']),
          _buildMealSection('Snacks', mealsData['snacks']),
        ],
      );
    }
  }

  Widget _buildMealSection(String mealName, dynamic items) {
    if (items == null) return const SizedBox.shrink();
    
    final itemList = items is List ? items : [];
    if (itemList.isEmpty) return const SizedBox.shrink();

    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            mealName,
            style: const TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 11,
              color: Colors.green,
            ),
          ),
          ...itemList.map((item) => Text(
                '  • ${item['food']} - ${item['quantity']}',
                style: const TextStyle(fontSize: 10),
              )),
        ],
      ),
    );
  }

  void _saveDietPlan() async {
    if (_selectedTemplateIndex == null) return;

    final template = widget.templates[_selectedTemplateIndex!];

    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:8000/api/diet/plan/create/'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'user_id': widget.userId,
          'trainer_id': widget.trainerId,
          'template_id': template['id'],
          'plan_name': template['name'],
          'target_calories': widget.targetCalories,
          'meals_data': template['meals_data'],
          'notes': _notesController.text.trim(),
          'start_date': DateTime.now().toIso8601String().split('T')[0],
        }),
      );

      final data = json.decode(response.body);

      Navigator.pop(context);

      if (response.statusCode == 201 && data['success'] == true) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Diet plan created for ${widget.userName}'),
            backgroundColor: Colors.green,
          ),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(data['message'] ?? 'Failed to create diet plan'),
            backgroundColor: Colors.red,
          ),
        );
      }
    } catch (e) {
      Navigator.pop(context);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error: $e'), backgroundColor: Colors.red),
      );
    }
  }
}
