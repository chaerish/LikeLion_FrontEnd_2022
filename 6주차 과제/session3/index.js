// const input=prompt();
// if (input===""){
//     console.log("입력값이 없습니다.")
// }else{
//     console.log(input);
// }
// const me={
//     name:'유예빈',
//     age:26,
//     gender:'male',
// };

// const someone={
//     name:'홍길순',
//     age:27,
//     gender:'female'

// };

// function addMsM(person){
//     if(person.gender=='male'){
//         person.militaryState=false;
//     }
// }

// // addMsM(me);
// // addMsM(someone);

// function parseBoolean(value){
// if(vaule===true){
//     return '참';
// }else if(vaule===false){
//     return '거짓';
// }
// }

// // if (me.militaryState!==undefined){
// //     console.log(parseBoolean(me.militaryState));
// // }

// me.militaryState!==undefined&&console.log(parseBoolean(me.militaryState)); //true->뒤에있는 consolelog가 실행됨 false-> 앞에값만 반환하고 뒤에는 실행되지않음 

// const iput=prompt();

// if(input===""){
//     console.lof("입력값이 없습니다.");
// }else{
//     console.log(input);
// }


// console.log(input||"입력값이 없습니다."); 

// const me={
//     name:"유예빈",
//     age:'26',
// };

// const {name}= me;  //비구조화 할당 
// const{age}=me;
// const{name,age}=me; //키값을 변수선언할때.. 

// const me={
//     name:"유예빈",
//     age:'26',
// };

// const me1={
//     ...me}; //흩뿌리기 spread 

// const animals=["개","고양이"];
// const animalss=[...animals,"참새"];
// //array 는 array에만 흩뿌리기 가능하고, 객체는 객체에만 가능 


const me={
    name:"유예빈",
    age:'26',
};

const{age,...another}=me; //age 제외하고 다른거를 추가 
//배열은 ...rest 
//제외할것,...another 로 해주면 된다.




