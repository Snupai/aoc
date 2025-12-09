## --- Part Two ---
The Elves just remembered: they can only switch out tiles that are **red** or **green**. So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it by a straight line of **green tiles**. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

Using the same example as before, the tiles marked `X` would be green:
<pre><code>
..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............
</code></pre>
In addition, all of the tiles **inside** this loop of red and green tiles are also green. So, in this example, these are the green tiles:
<pre><code>
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
</code></pre>
The remaining tiles are never red nor green.

The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

For example, you could make a rectangle out of red and green tiles with an area of `15` between `7,3` and `11,1`:
<pre><code>
..............
.......OOOO<span style="font-weight:bold">O</span>..
.......OOOOO..
..#XXXX<span style="font-weight:bold">O</span>OOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
</code></pre>
Or, you could make a thin rectangle with an area of `3` between `9,7` and `9,5`:
<pre><code>
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX<span style="font-weight:bold">O</span>XX..
.........OXX..
.........<span style="font-weight:bold">O</span>X#..
..............
</code></pre>
The largest rectangle you can make in this example using only red and green tiles has area `24`. One way to do this is between `9,5` and `2,3`:
<pre><code>
..............
.......#XXX#..
.......XXXXX..
..<span style="font-weight:bold">O</span>OOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOO<span style="font-weight:bold">O</span>XX..
.........XXX..
.........#X#..
..............
</code></pre>
Using two red tiles as opposite corners, **what is the largest area of any rectangle you can make using only red and green tiles?**