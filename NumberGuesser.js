let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
function generateTarget() {
  return Math.round(Math.random()*9);
}

function compareGuesses(human, computer, secret) {
  humanDiff = Math.abs(secret - human);
  computerDiff = Math.abs(secret - computer);
  if (humanDiff <= computerDiff) {
    return true;
  } else {
    return false;
  }
}

function updateScore(winner) {
  if (winner === "human") {
    humanScore += 1;
  } else {
    computerScore += 1;
  }
}

function advanceRound() {
  currentRoundNumber += 1;
} 
