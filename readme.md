# About
This is a demo of a program I wrote using Python and the NEAT library. Majority of the coding was
done by me with refrances and ai only being used when encountering genuin stumps and roadblocks and used stickly
to explain rather than do it for me. The goal was to learn how to use NEAT, so I made a challange for myself to
learn it and impliment it into a program in a weekend + a day.


## Files
snake.py - the main file i used to design the game and train the genomes. Running it will result 
in "best_snake.pkl" to be updated. The program runs the genome with the best fitness at the end, if it
performed well, the file can be saved by renaming it. This new file can then be rerun in "snake_demo.py".

snake_demo.py - is a stripped version of "snake.py" which removed the training part of the file and just lets 
me rerun a previous pickle file. 


## Note

The location of the apple spawns does not save, so while thethe saved genome is trained, the results can 
still be inconsistent. I've provided some seeds where the genome performed well. See 14 with "best_snake_16735". 
You can select use differen pkl files in the snake_demo file by changing the name on line 52. 

Also, a large chunck of code in snake.py is commented out. That was used to render each genmoe of each generation
but I have since commented it out and reduced clock tick to O so that I don't have to watch each train.


NEAT and genomes - The genome saved in the pickle file is what I considered to be a run with a high fitness, 
meaning it performed well relative to other attempts.

## Challenges
One of the challenges I faced with this project was getting familiar with NEAT and how 
it worked. Before snake, my only experience with NEAT was a top down car racing demo I had taken from a tutorial
on Youtube. While I did a good job introducing NEAT as a concept, I did not teach me how to impliment it into a
unique program from scratch. Another challenge I ran into was the snake being able to know where it's tail and
body is. While I did figure out collision when developing the actual snake game, I could not figure out how
to translate for NEAT. I could have used an LLM to find a solution, but I deamed that to be to substancial of a
modification to my code, and I wouldn't feel comfortable calling it my own work. However, I do see potential to
revisit in the future. This project was a weekend challenge I had made for myself to teach me about NEAT. 

'''
pip install pygame neat-python
