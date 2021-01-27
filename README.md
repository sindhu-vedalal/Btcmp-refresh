# Python-games-beginners
## The repository
This repository is where we add games that python beginners can learn from.

## Contributing
<p>There are many ways in which you can contribute to the repository:
  <ul>
    <li> Want to add code for an advanced game? Need longer time than the average small game? Follow "Branching strategy for a long term feature"
    <li> Got a bunch of easy games you'd like to add? Follow "Github flow workflow"."
    <li> Think you've found a problem with one of the games? *Yikes!* Follow "github flow workflow

  </ul>
</p>

### Branching startegy - Gtihub flow workflow for short features and hotfixes
<p>
In short - create a copy and record all changes to that copy.
Create a new feature branch and in it add your new game.
Once your game is complete, create a pull request to merge your game into the repo.
Makke sure to name you branch feature-*feature-name* for short features and hotfix-* to fix bugs
</p>


<p>
References:
<ul>
  <li><a href="https://pradeeploganathan.com/git/git-branching-strategies/">1</a>
  <li><a href="https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf">2</a>
</ul>
</p>.

### Branching strategy for a long term branches
  <p>
    The recommended approach for long term feature is to periodically keep merging with the development branch (merging from one branch into another multiple times over a long period ).
    Merge in increments until the entire feature is complete and ready to merge into master.
    </p>

  <p>
    References: <a href="https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows">3</a>
  </p>



## Before you merge

<p>
    To make sure that all code in the repo follows the same coding format, pre-commit checks are in place.
    Everytime you try to commit - pre-commit script runs to make sure your commit follow the standard.</p>
<p>
    Follow installation instructions <a href="https://pre-commit.com/#install"> here </a>
</p>
    Once installed, make sure the .pre-commit-config.yaml file specifies the standards to follow.
    Run pre-commit install in your git repo to link the pre-commit hooks. [Hooks are generally found in <repo>/.git/hooks]
    Your pre-commit hooks are ready!



</p>

## Cherry picking a specific game
    To pull specific changes from a branch use cherry picking.
    Use the commit hash (find the commit hash through git log) to pickup a specific change.

    Usage:
    git cherry-pick *commit-hash*

    Make sure you are already on the branch onto which you want to cherry pick the change.

## Rebasing
  Rebasing rewrites your git history to put all the commits in their proper place in time - with merge you have your original commits plus merge history, with cherry picking, the commits are written right on to the branch you are rebasing into - harder to undo.
  
  Usage:
  git rebase -i *branch-name*

  WE recommend merging over rebasing for this repo.

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
