# echols-portfolio
A brief collection of my academically- and recreationally-motivated Python projects. 

My most extensive individual coding project is the VUSA (Very unfriendly seating algorithm) which informed my undergraduate thesis, "The very unfriendly seating arrangement problem". The thesis PDF and two self-contained Python files (including some explanation of the process) are included.

Most recently is my work on circulant graphs for my Doctoral Dissertation. The corresponding PDF is "Periodic orbits on 2-regular circulant digraphs". The program "Primitive Periodic Orbits Counter" is straightforward; it takes formulae proven in the paper and calculates them for arbitrary parameters.

Lastly are my fun projects. 

"Draw Puzzle" is a project I did in the summer between undergrad and graduate school. My family was working on a jigsaw puzzle and the monochrome sky had been uncompleted. I found it amusing to try and fill it in algorithmically. It seemed most effective to start with the holes that had three completed neighbors and test every piece whose innie-outie profile would match (though, I did not pay any mind to the precise shape of the 3 known sides until the exact match snapped into place). I began to wonder what the most efficient approach would actually be. After trying some game-tree calculations on very small puzzles, I realized the approach would probably depend on knowing the exact distribution of the shapes (a 4x3 puzzle with the inner 2 pieces having all innies has many rotations, whereas some border shapes make the remaining 2 pieces automatic). I began trying to build a program to test over several trials. This little program makes a random puzzle (easy enough) but it ALSO tracks each piece in a matrix, knowing which sides of each entry are innies or outies. 

"ChaoticAttractor" is a famous example https://www.youtube.com/watch?v=kbKtFN71Lfs. I made this little thing for practice when I was teaching myself Python during my undergrad thesis.
