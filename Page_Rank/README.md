Page_Rank

This program is used to calculate the page ranks from a file provided.
The file provide should have pairs of numbers seprated by a space. 
The first number is where it is comming from and the second is where it is going to
This implementation does not have Random Teleportation implemented

The results are saved to results directory with with results_ followed by the original file name
A sample of the results returned follows

Data directory stores all the original files this was tested on.

run test: python -m pytest -v

run program: python src/page_rank.py


##############
Sample Results
##############

Results for graph3V.txt

With denomanator limited to less than 100,000
it took 13 iterations

Graph of Connections
 X axis: Page From
 Y axis: Page To
 Divided By number of connections

     :0:  :1:  :2: 
  :0: 1/2  1/2  0    
  :1: 1/2  0    1    
  :2: 0    1/2  0    


Vertix ID, PageRank Value
        0,0.397     
        1,0.407     
        2,0.196     

iter page 0         page 1         page 2         
  0: 1/3            1/3            1/3            
  1: 1/3            1/2            1/6            
  2: 5/12           1/3            1/4            
  3: 3/8            11/24          1/6            
  4: 5/12           17/48          11/48          
  5: 37/96          7/16           17/96          
  6: 79/192         71/192         7/32           
  7: 25/64          163/384        71/384         
  8: 313/768        73/192         163/768        
  9: 605/1536       213/512        73/384         
 10: 311/768        1189/3072      213/1024       
 11: 811/2048       1261/3072      1189/6144      
 12: 4955/12288     4811/12288     1261/6144      
 13: 4883/12288     3333/8192      4811/24576     
