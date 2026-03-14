import 'package:flutter/material.dart';
class AddScreen extends StatelessWidget {
  const AddScreen({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () => Navigator.pop(context),
        ),
        title: const Text('Add Task'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.create),
            onPressed: () {
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            //..........Esli bi tolko komentarii zelenie bili
            const Text('Task name', style: TextStyle(fontWeight: FontWeight.bold)),
            const SizedBox(height: 10),
            TextField(
              decoration: InputDecoration(
                hintText: 'Enter the task name',
                border: UnderlineInputBorder(),
                //border: OutlineInputBorder(borderRadius: BorderRadius.circular(15.0),)
              ),
            ),

            //desc
            const SizedBox(height: 25),
            const Text(
              'Description', style: TextStyle(fontWeight: FontWeight.bold),),
            const SizedBox(height: 10),
            TextField(
              maxLines: 5,
              decoration: InputDecoration(
                hintText: 'Enter task description',
                
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(15.0),),
              ),
            ),
            
            //categor
            const SizedBox(height: 25,),
            const Text('Task Category', style: TextStyle(fontWeight: FontWeight.bold),),
            const SizedBox(height: 10),
            Row(mainAxisAlignment: MainAxisAlignment.start,
              children: [
                _buildCategoryIcon(Icons.work, "Work", Colors.grey),
                const SizedBox(width:10),
                _buildCategoryIcon(Icons.person, "Personal", Color(0xFFF3701E)),
                const SizedBox(width:10),
                _buildCategoryIcon(Icons.school, "Study", Colors.grey),
                const SizedBox(width:10),
                _buildCategoryIcon(Icons.favorite, "Other", Colors.grey),
              ],
            ),

            //calend
            const SizedBox(height: 25,),
            const Text('To do before', style: TextStyle(fontWeight: FontWeight.bold),),
            const SizedBox(height: 10),
            InkWell(
              onTap: (){},
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 15),
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey),
                  borderRadius: BorderRadius.circular(15),
                ),
                child: const Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text('Choose date', style: TextStyle(color: Colors.grey),),
                    Icon(Icons.calendar_today, color: Colors.grey,)
                  ],
                )
              ),
            ),

            //prior
            const SizedBox(height:25),
            const Text('Priority', style: TextStyle(fontWeight: FontWeight.bold),),
            const SizedBox(height:10), 
            // Row(
            //   mainAxisAlignment: MainAxisAlignment.spaceBetween,
            //   children: [
            //     Expanded(
            //       child: _buildPriorityChipStatic('Low', Colors.green, true),
            //     ),
            //     const SizedBox(width: 8),
            //     Expanded(
            //       child: _buildPriorityChipStatic('Medium', Colors.yellow, false),
            //     ),
            //     const SizedBox(width: 8),
            //     Expanded(child: _buildPriorityChipStatic('High', Colors.red, false),
            //     ),   
            //   ],
            // ),
            Row( 
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                _buildPriorityChipStatic('Low', Colors.green, true),
                const SizedBox(width:10),
                _buildPriorityChipStatic('Medium', Colors.yellow, true),
                const SizedBox(width:10),
                _buildPriorityChipStatic('High', Colors.red, true),
              ],
            ),
            // const SizedBox(height:25),
            // SizedBox(
            //   width: double.infinity,
            //   height: 55,
            //   child: ElevatedButton(
            //     onPressed: () {
            //       Navigator.pop(context);
            //     },
            //     style: ElevatedButton.styleFrom(
            //       backgroundColor: Theme.of(context).colorScheme.primary,
            //       foregroundColor: Theme.of(context).colorScheme.onPrimary,
            //       shape: RoundedRectangleBorder(
            //         borderRadius: BorderRadius.circular(15),
            //       ),
            //     ),
            //     child: const Text('Add', 
            //         style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            //   ),
            // ),
            
          ],
        )
      ),

      //Add button
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.fromLTRB(20, 0, 20, 30), 
        child: SizedBox(
          width: double.infinity,
          height: 55,
          child: ElevatedButton(
            onPressed: () => Navigator.pop(context),
            style: ElevatedButton.styleFrom(
              backgroundColor: Theme.of(context).colorScheme.surface,
              foregroundColor: Theme.of(context).colorScheme.onPrimary,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(15),
                side: BorderSide(
                  color: Theme.of(context).colorScheme.secondary,
                  width: 1.5,
                ),
              ),
            ),
            child: const Text('Add', 
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          ),
        ),
      ),

    );
  }
  Widget _buildCategoryIcon(IconData icon, String label, Color color) {
    return Column(
      children: [
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            //color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: color, width: 1.5)
          ),
          child: Icon(icon, color: color),
        ),
        const SizedBox(height: 5),
        Text(label, style: const TextStyle(fontSize: 12, color: Colors.grey)),
      ],
    );
  }
  Widget _buildPriorityChipStatic(String label, Color color, bool isSelected) {  
    return ChoiceChip(
      label: Text(label),
      selected: isSelected, 
      onSelected: (bool selected) {},
      selectedColor: color.withAlpha(150),
      checkmarkColor: color,
      //padding: const EdgeInsets.symmetric(horizontal:20, vertical:8),
      labelStyle: TextStyle(
        color: isSelected ? color : Colors.grey,
        fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
      ),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10),
      ),
      side: BorderSide(
        color: isSelected ? color : Colors.grey.shade300,
      ),
    );
  }
}
//ne prigodilos
//enum Categ { work, personal, study, shopping }
