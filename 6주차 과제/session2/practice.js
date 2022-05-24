// document.getElementById('lion').style.color='red';
// const animal=document.getElementByTagName("li") //인수에 들어있는 태그 이름을 갖는 모든 요소 노드들을 탐색해 반환한다.
// document.getElementByTagName("li")[0].style.color='red'; 

// document.getElementsByClassName("animal")[1].style.color="red"; //클래스를 이용한 요소 노드 취득.

// document.querySelector('css선택자')
// document.querySelectorAll('css선택자')
// document.querySelectorAll('.animal')[0].getElementsByClassName.color="red";

//DOM 조작
// document.querySelectorAll(".animal")[2].innerHTML="dog";
// const animals=document.getElementById("animals");
// animals.innerHTML+="<li class='animals'>cat</li>" //cat 추가 

// document.querySelectorAll(".box")[0].classList.add("purple"); //remove -> 제거 
// document.querySelectorAll(".box")[0].classList.toggle("yellow") 
// toggle 한 번 더 쓰면 제거됨..? 다시 클릭시 생성 

// document.getElementById('btn').addEventListener("click",function(){
//     console.log("click!");
// });//버튼 눌렀을 때, 클릭이라고 출력 

// var num=0;
// document.getElementById('plus').addEventListener("click",function(){
//     num++;
//     document.getElementById("num").innerHTML=num;
// });
// document.getElementById('minus').addEventListener("click",function(){
//     num--;
//     document.getElementById("num").innerHTML=num;
// });

// document.querySelector(".bar").addEventListener("click",function(){
//     document.querySelector(".newBar").style.display="block";
// });

// document.querySelector(".bar").addEventListener("click",function(){
//     document.querySelector(".newBar").classList.toggle("show");
// });
// document.querySelector(".bar").addEventListener("click",function(){
//     document.querySelector(".bar").innerHTML="눌렀어!";
//     document.querySelector(".newBar").classList.toggle("show");
// }); //이벤트 타입(click), 이벤트 핸들러(function)

// document.querySelectorAll('.list')[0].addEventListener("click",tabBtn(e,target.dataset.id));

// function tabBtn(a){
//     document.querySelectorAll(".tab-button")[0].addEventListener("click",function(){

//         for(let i=0;i<document.querySelectorAll("tab-button"). length; i++){ //길이만큼 i가 하나씩 늘어남 
//             document.querySelectorAll('.tab-button')[i].classList.remove("here")
//             document.querySelectorAll('.tab-content')[i].classList.remove("show")
//         } //here,show 하나씩 없애줌 
    
//         document.querySelectorAll('.tab-button')[a].classList.add("here")
//         document.querySelectorAll('.tab-button')[a].classList.add("show")
    
//     });

   
// }

//scroll 이벤트 보여지는 부분 clientHeight , 전체 scrollHeight