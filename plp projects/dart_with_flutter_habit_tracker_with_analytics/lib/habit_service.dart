import 'package:flutter/foundation.dart';
import 'habit_model.dart';

class HabitService extends ChangeNotifier {
  List<Habit> _habits = [];

  List<Habit> get habits => _habits;

  void addHabit(Habit habit) {
    _habits.add(habit);
    notifyListeners();
  }

  void markHabitComplete(int index) {
    if (_habits[index].completed) return;
    _habits[index].completed = true;
    _habits[index].streak++;
    notifyListeners();
  }

  void resetHabit(int index) {
    _habits[index].completed = false;
    notifyListeners();
  }

  double getCompletionRate() {
    if (_habits.isEmpty) return 0;
    int completedCount = _habits.where((habit) => habit.completed).length;
    return (completedCount / _habits.length) * 100;
  }
}
