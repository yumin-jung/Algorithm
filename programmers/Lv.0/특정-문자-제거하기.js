function solution(my_string, letter) {
    return my_string.split("").filter((elem) => {
        return elem !== letter;
    }).join("");
}