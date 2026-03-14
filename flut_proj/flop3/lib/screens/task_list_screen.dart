import 'package:flutter/material.dart';
class ListScreen extends StatelessWidget {
  const ListScreen({super.key});
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
      body: ListView.builder(
        padding: const EdgeInsets.all(8.0),
        itemCount: 10,
        itemBuilder: (context, index) {
          return Card(
            margin: const EdgeInsets.symmetric(vertical:4.0, horizontal: 8.0),
            child: ListTile(
              leading: Checkbox(
                value: index % 2 == 0, 
                onChanged: (value) {
                },
              ),
              title: Text('Task ${index + 1}'),
              subtitle: Text('Created:'),
              trailing: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(
                    index % 3 == 0 ? Icons.work :
                    index % 3 == 1 ? Icons.person : Icons.school
                  ),
                  IconButton(
                    icon: const Icon(Icons.delete, color: Color(0xFFad0013)),
                    onPressed: () {},
                  ),
                ],
              ),
              onTap: () {
                Navigator.pushNamed(
                  context,
                  '/details',
                  arguments: "Task"
                );
              }
            ),
          );
        },
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: 0,
        type: BottomNavigationBarType.fixed,
        onTap: (index) {
          if (index == 1) {
            Navigator.pushNamed(context, '/add');
          }
        },
        items: const [
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
      ),
    );
  }
}