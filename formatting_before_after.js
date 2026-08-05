// ============================================================
// BEFORE: messy, unformatted code with real ESLint issues
// ============================================================
// Running `npx eslint` on this section originally found 11 problems,
// including a real bug: `goal=30` was an assignment, not an argument.
//
var  focusMinutes = 45
let userName = "koushik"
function calc( minutes,goal ) {
     if(minutes>goal)
    {
        return "goal met"
    }
    else{
       return "goal not met"
   }
}
 console.log( calc(focusMinutes,goal=30) )

 const arr=[1,2,3,4,5]
 arr.forEach(function(x){
 console.log(x)
 })
 let unused = "never used";

// ============================================================
// AFTER: formatted with Prettier, fixed with ESLint (0 errors, 0 warnings)
// ============================================================

const focusMinutes = 45;

function calc(minutes, goal) {
  if (minutes > goal) {
    return 'goal met';
  }
  return 'goal not met';
}

// eslint-disable-next-line no-console
console.log(calc(focusMinutes, 30));

const arr = [1, 2, 3, 4, 5];
arr.forEach((x) => {
  // eslint-disable-next-line no-console
  console.log(x);
});
