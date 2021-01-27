# Python-games-beginners
## The repository
This repository is where we add games that python beginners can learn from.

## Contributing
<p>There are many ways in which you can contribute to the repository:
  <ul>
    <li> Want to add code for an advanced game? Need longer time than the average small game? Follow *branching strategy* 
    <li> Got a bunch of easy games you'd like to add? Follow *branching strategy*
    <li> THink you've found a problem with one of the games? *Yikes!* Follow *branching strategy*
      
  </ul>
</p>

## Before you merge

<p> 
    To make sure that all code in the repo follows the basic coding practices, we have pre-commit checks in place.
    All code must have a pylint score of 9 or above.


</p>

## Cherry picking a specific game
*cheery picking and rebasing*

## Monorepo
  <p>
  All code related to one org(multiple projects) in a single repository.

  ### Pros
  <ul> 
    <li> Reusbility - easy
    <li> Dependencies optimized
    <li> Refactoring on a large scale
    <li> Flexible ownership - collaboration 
  </ul> 


  ### Cons
  <ul>
    <li> All changes to one project refect in the commit history for the repo - sub tree -> tree (managing unrelated projects on a single tree)
    <li> Larger number of branches/tags affect performance (performance takes a hit when performing basic git operations)
    <li> Large files in a single subtree affect the performance of the entire repo
  </ul>
  </p>
