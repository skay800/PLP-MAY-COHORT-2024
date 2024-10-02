// lib/analytics_page.dart

import 'package:flutter/material.dart';
import 'habit_service.dart';

class AnalyticsPage extends StatelessWidget {
  final HabitService habitService;

  AnalyticsPage({required this.habitService});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Analytics')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Completion Rate: ${habitService.getCompletionRate().toStringAsFixed(2)}%'),
          ],
        ),
      ),
    );
  }
}
