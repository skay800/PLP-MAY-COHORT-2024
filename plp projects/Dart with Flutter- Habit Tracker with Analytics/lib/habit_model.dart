// lib/habit_model.dart

class Habit {
  final String name;
  bool completed;
  int streak; // Count of consecutive completions

  Habit({required this.name, this.completed = false, this.streak = 0});
}
