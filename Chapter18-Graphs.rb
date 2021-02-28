#!/usr/bin/ruby
#Chapter18
#Q4:
def​ bfs​(starting_vertex, search_value)
​     queue = Queue.​new​
​
​     visited_vertices = {}
​ 	  visited_vertices[starting_vertex.​value​] = ​true​
​ 	  queue.​enqueue​(starting_vertex)
​
​ 	  ​while​ queue.​read​
​ 	    current_vertex = queue.​dequeue​
       return current_vertex.value if current_vertex.​value​ == search_value
​ 	    current_vertex.​adjacent_vertices​.​each​ ​do​ |adjacent_vertex|
​​ 	      ​if​ !visited_vertices[adjacent_vertex.​value​]
​​ 	        visited_vertices[adjacent_vertex.​value​] = ​true​
​​ 	        queue.​enqueue​(adjacent_vertex)
​ 	      ​end​
​ 	    ​end​
​ 	  ​end​
     return nil
​ 	​end​

#Q5:
def​ shortestConnection(starting_vertex, final_vertex)
​     queue = Queue.​new​
​     previous_vertex_table = {}
​     visited_vertices = {}
​ 	  visited_vertices[starting_vertex.​value​] = ​true​
​ 	  queue.​enqueue​(starting_vertex)
​
​ 	  ​while​ queue.​read​
​ 	    current_vertex = queue.​dequeue​
​ 	    current_vertex.​adjacent_vertices​.​each​ ​do​ |adjacent_vertex|
​​ 	      ​if​ !visited_vertices[adjacent_vertex.​value​]
​​ 	        visited_vertices[adjacent_vertex.​value​] = ​true​
​​ 	        queue.​enqueue​(adjacent_vertex)
          previous_vertex_table[adjacent_vertex.value] = current_vertex.value
​ 	      ​end​
​ 	    ​end​
​ 	  ​end​

​ 	  shortest_path = []
     current_person_value = final_vertex.​value
​
​ 	  ​while​ current_person_value != starting_person.​value
​
​ 	    shortest_path << current_person_value
​ 	    current_person_value = previous_vertex_table[current_person_value]
​ 	  ​end​​
​ 	  shortest_path << starting_person.​nvalue
​
​ 	  ​return​ shortest_path.​reverse​
​ 	​end​
