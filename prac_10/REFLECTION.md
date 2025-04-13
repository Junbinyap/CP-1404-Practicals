# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

Some tasks took longer than I expected because it is difficult just like the html question of prac 10,
while others were quicker than I thought.

### How did your estimate accuracy improve or change during the course of the subject?

As the subject progressed, I became more realistic with my estimates. I started considering time for testing and unexpected bugs
which made my estimates more accurate.

### What did you learn from doing these estimates?

I learned the importance of planning ahead and breaking down problems into smaller parts

## Code Reviews

### What have you learned from being reviewed by other people?

Sometimes reviewers pointed out issues or improvements I had completely missed. Their feedback helped me write cleaner and more readable code.

### What have you learned from doing code reviews of other people?

Reviewing others’ code helped me better understand good coding practices and different ways to solve the same problem

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

[class Band:
     """Band class to manage a collection of Musicians."""

     def __init__(self, name):
         """Initialise a Band with a name and an empty list of musicians."""
         self.name = name
         self.musicians = []
 
     def add(self, musician):
         """Add a Musician to the Band."""
         self.musicians.append(musician)
 
     def __str__(self):
         """Return string representation of the Band and its Musicians."""
         musician_strings = ", ".join(str(musician) for musician in self.musicians)
         return f"{self.name} ({musician_strings})"
 
     def play(self):
         """Return string of each Musician playing or needing an instrument."""
         return "\n".join(musician.play() for musician in self.musicians)]()

### Explanation

He did well in this prac as he follow all the structure and expected and have the expected output

### Good Code Review 2

 
     languages = [ruby, python, visual_basic]
     print("The dynamically typed languages are:")
     for language in languages:
         if language.is_dynamic():
             print(language.name)


### Explanation

he did well and have a good understanding in for loop

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?
I would provide a few more example solutions.

### What did you do really well for practicals in this subject?
I was consistent with completing all practicals on time.  I made sure my code was neat, well-commented
