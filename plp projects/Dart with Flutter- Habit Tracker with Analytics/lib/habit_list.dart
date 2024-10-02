// lib/habit_list.dart

import 'package:flutter/material.dart';
import 'habit_service.dart';
import 'habit_model.dart';
import 'analytics_page.dart';

class HabitList extends StatelessWidget {
  final HabitService habitService;

  HabitList({required this.habitService});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Habit Tracker'),
        actions: [
          IconButton(
            icon: Icon(Icons.analytics),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => AnalyticsPage(habitService: habitService),
                ),
              );
            },
          ),
        ],
      ),
      body: ListView.builder(
        itemCount: habitService.habits.length,
        itemBuilder: (context, index) {
          final habit = habitService.habits[index];
          return ListTile(
            title: Text(habit.name),
            trailing: Checkbox(
              value: habit.completed,
              onChanged: (bool? value) {
                if (value != null) {
                  habitService.markHabitComplete(index);
                  (context as Element).markNeedsBuild(); // Rebuild the widget
                }
              },
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _showAddHabitDialog(context);
        },
        child: Icon(Icons.add),
      ),
    );
  }

  void _showAddHabitDialog(BuildContext context) {
    final TextEditingController controller = TextEditingController();

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text('Add New Habit'),
          content: TextField(
            controller: controller,
            decoration: InputDecoration(hintText: 'Habit name'),
          ),
          actions: [
            TextButton(
              onPressed: () {
                if (controller.text.isNotEmpty) {
                  habitService.addHabit(Habit(name: controller.text));
                  Navigator.of(context).pop();
                }
              },
              child: Text('Add'),
            ),
          ],
        );
      },
    );
  }
}
