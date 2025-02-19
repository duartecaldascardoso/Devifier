Ideas:

- Agent workflow to create new questions
- Add an external link to learn more about the mentioned subject in the question

TO-DO:

- back-end layer using Django models
- set up local instance of an LLM to create new questions
- consider using LLM to provide website information for questions

Business logic:

- consider how to monetize the solution
- evaluate the number of challenges available per day
- product description will be: chess puzzles for programming

User relation with Puzzles:

The user will be able to solve different Puzzles. This will be a continuous effort and upon solving one, the system will determine which puzzle to solve next (similarly to [chess.com](http://chess.com) Puzzles)

The puzzle that is presented right after must never be the same as the one before. Therefore we should at least keep them in the state (preserve all the ids of the puzzles that were solved recently)

Should the puzzles be created in a different way according to if they are open answer or multiple choice? 

Idea: create a Puzzle abstract class and then create classes for MultipleChoicePuzzle and OpenAnswerPuzzle 

When selecting a next Puzzle, we will simply use the abstract class, everything else does not matter. We should have different UI methods for the Multiple choice and Open answer questions. 

To be shown to the user after a Puzzle has been solved:

- Correct answer
- Link to a website that addresses the topic
- His rating change → and subsequently the current rating

The user shall be able to select the puzzles he wants to do by:

- Rating level
- Tag
- Language

The user should have access to an unrated queue → this means that he can simply practice without worrying about his rating.