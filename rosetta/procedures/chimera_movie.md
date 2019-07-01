# How to Record Movie in Chimera
## Dreycey Albin

## Download

Go to the following website to download the software:
https://www.cgl.ucsf.edu/chimera/download.html

The rest of this tutorial use to favorites command line in chimera, here are
instructtons on how to use this:
https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/getting_started.html

Essentially, all you have to do is go to the tab labeled "Favorites" then go to
the "command line". This is where you can insert commands for the following. I
have also sent you a pdb that these commands should work on.

## Recording

https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/midas/movie.html

To being recording you use: `movie record`
To finish recording use: `movie encode`

These commands can have other commands in between, such as:

```
movie record ; turn y 1 360 ; wait; turn x -1 90; wait ; ~ribbon; ~disp :11-70; turn y 1 10; turn y -1 10; wait; ~disp :90,89; distance :10@N1 :71@N1; reset pos1 50; wait; color green :10@N1 :71@N1; turn y 1 360; wait; movie encode
```

## Move Model

https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/midas/move.html

To move model, it all depends on x,y,z axis of rotations.

 * To move x `move x 1 5`
 * To move y `move x 1 5`
 * To move z `move x 1 5`

To turn model, it all depends on x,y,z axis of rotations.

 * To turn x `turn x 1 5`
 * To turn y `turn x 1 5`
 * To turn z `turn x 1 5`

This can be used while recording:

```
movie record ; turn y 1 360 ; wait; turn x -1 90; wait ; turn y 1 10; turn y -1 10; wait; turn y 1 360; wait; move x 5 5, movie encode
```

## Zoom In

https://www.cgl.ucsf.edu/chimera/docs/usersguide/midas/savepos.html

Zoom in on the frame that you like, then enter: `set`

Command I use: `savepos pos1`

Then you can zoom in on this frame using (when in different frame): `reset pos1 50`

This can be used while recording:

```
movie record ; turn y 1 360 ; wait; reset pos1 50; wait; turn y 1 360; wait; movie encode
```

## Color

https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/midas/color.html

To color (or go to) specific positions, the following syntax is used:

 * `#` is is MODELNUMEBER
 * `:` is the residue
 * `@` is the atom

For example: `color green #1:10@N1 #2:71@N1`

This colors the `N1` positions of two different models in chimera green.

This can be used while recording:

```
movie record ; turn y 1 360 ; wait; color green :10@N1 :71@N1; movie encode
```
