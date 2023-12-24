<h1>Match</h1>
<h4>Result before:</h4>
<p>On this current function a linear search algorithm was implemented with time complexity Omega(n1*n2)</p>
<img src=img/before.JPG>

<h4>Result after:</h4>
<p> To optimize the search I use set interaction so now the time complexity is Omega(min(len(n1), len(n2)))</p>

 ```python
   return set(fave_numbers_1) & set(fave_numbers_2) == set(fave_numbers_2)
 ```

<img src=img/after.JPG>

