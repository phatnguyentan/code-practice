let str = "abcde";
let choices = [];
function combination(choice) {
    for(let i = choice; i < str.length; i++) {
        if(choices[i]) continue;
        choices.push(i);
        let s = "";
        choices.forEach(c => {
            s = s + str[c];
        });
        console.log(s);
        if(i + 1 < str.length) {
            combination(i + 1);
        }
        choices.pop();
    }
}
combination(0);