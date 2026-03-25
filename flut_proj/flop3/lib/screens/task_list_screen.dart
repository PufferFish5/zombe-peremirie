import 'package:flutter/material.dart';
import '../models/task.dart';
class ListScreen extends StatefulWidget {
  const ListScreen({super.key});
  @override
  State<ListScreen> createState() => _ListScreenState();
}

class _ListScreenState extends State<ListScreen> {
  List<Task> _tasks = [];
  @override
  void initState() {
    super.initState();
    _tasks = [
      Task(
        id: '1', 
        title: 'test1', 
        description: 'desc1', 
        category: 'Personal', 
        date: DateTime.now(),
        priority: 'High',
      ),
      Task(
        id: '2', 
        title: 'test2', 
        description: 'desc2', 
        category: 'Work', 
        date: DateTime.now(),
        priority: 'Medium'
      ),
    ];
  }

  void _addTask(Task task) {
    setState(() {
      _tasks.add(task);
    });
  }

  void _toggleTaskStatus(String id) {
    setState(() {
      final index = _tasks.indexWhere((task) => task.id == id);
      if (index != -1) {
        _tasks[index].isCompleted = !_tasks[index].isCompleted;
      }
    });
  }

  void _deleteTask(String id) {
    setState(() {
      _tasks.removeWhere((task) => task.id == id);
    });
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('My Tasks'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
            onPressed: () {
            },
          ),
        ],
      ),
      body: _tasks.isEmpty 
      ? const Center(child: Text("There's nothing to do"))
      : ListView.builder(
        itemCount: _tasks.length,
        itemBuilder: (context, index) {
          final task = _tasks[index];
          return Card(
            margin: const EdgeInsets.symmetric(horizontal: 15, vertical: 5),
            color: Theme.of(context).colorScheme.surface.withAlpha(50),
            child: ListTile(
              leading: Checkbox(value: task.isCompleted, onChanged: (value) {_toggleTaskStatus(task.id);}),
              title: Text(
                task.title,
                style: TextStyle(
                  decoration: task.isCompleted ? TextDecoration.lineThrough : TextDecoration.none,
                ),
              ),
              subtitle: Text(task.category),
              trailing: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  // Icon(Icons) potom potom nado chekanie na tip zadachi
                  IconButton(
                    onPressed: () {_deleteTask(task.id);}, 
                    icon: const Icon(Icons.delete, color: Colors.red,)
                  ),

                ]
              )
            ),
          );
        },

      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: 0,
        type: BottomNavigationBarType.fixed,
        onTap: (index) async {
          if (index == 1) {
            final dynamic result = await Navigator.pushNamed(context, '/add');
            if (result != null && result is Task) {
              _addTask(result);
            }
          }
        },
        items: [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Tasks',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.add_circle, size: 40),
            label: 'Add',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
        backgroundColor: Theme.of(context).colorScheme.primary,
      ),
    );
  }
}
