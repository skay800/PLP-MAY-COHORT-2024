// lib/main.dart

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'habit_service.dart';
import 'habit_list.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => HabitService(),
      child: MaterialApp(
        title: 'Habit Tracker',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: HabitList(habitService: HabitService()),
      ),
    );
  }
}
