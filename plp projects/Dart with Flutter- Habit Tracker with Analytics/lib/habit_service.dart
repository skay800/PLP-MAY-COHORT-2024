// lib/habit_service.dart

import 'habit_model.dart';

class HabitService {
  List<Habit> _habits = [];

  List<Habit> get habits => _habits;

  void addHabit(Habit habit) {
    _habits.add(habit);
  }

  void markHabitComplete(int index) {
    if (_habits[index].completed) return;
    _habits[index].completed = true;
    _habits[index].streak++;
  }

  void resetHabit(int index) {
    _habits[index].completed = false;
  }

  double getCompletionRate() {
    if (_habits.isEmpty) return 0;
    int completedCount = _habits.where((habit) => habit.completed).length;
    return (completedCount / _habits.length) * 100;
  }
}
