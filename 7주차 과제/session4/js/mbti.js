const main=document.querySelector("#main");
const qna=document.querySelector("#qna");
const result=document.querySelector('#result');

const endPoint=10;

const select=[0,0,0,0]

//qna 넣기 
function addAnswer(answerText,qIdx,idx){
    var a=document.querySelector(".aBox");
    var answer=document.createElement('button');
 // 답변마다 클래스 추가해줌 
    answer.classList.add('answerList'); //버튼 꾸미기 
    answer.classList.add('my-5');
    answer.classList.add('py-3');
    answer.classList.add('mx-auto');

    answer.classList.add('fadeIn'); //애니메이션 효과 추가 

    a.appendChild(answer); //answer이 a에 소속됨 
    answer.innerHTML=answerText;

    //클릭시 다음으로 넘어가기 
    answer.addEventListener("click",function(){

        var children=document.querySelectorAll('.answerList'); 
        for(let i=0; i<children.length;i++){
            children[i].disabled=true;
            children[i].style.WebkitAnimation="fadeOut 0.5s";
            children[i].style.animation="fadeOut 0.5s";

        }
        setTimeout(()=>{ //애니메이션 효과를 주기(바로 사라지면 좀..어색?하다 )

            //타켓 타입별 넓혀줌 
            var target=qnaList[qIdx].a[idx].type;
            for( let i=0;i<target.length;i++){
                select[target[i]]+=1
            }

            for(let i=0;i<children.length;i++){
                children[i].style.display='none'; //그 전 거는 사라진다. 
            }
            goNext(++qIdx); //사라진 다음 다음으로 넘어감 
        
        },450) //450초 
    },false) //boolean 값 false 

}
function calResult(){ //가장 큰 결과값 반환 
    var result=select.indexOf(Math.max(...select));
    return result;
}

function setResult(){ //result 화면 설정 

    let point=calResult(); 
    //포인트에 맞는 것들 출력해줌 

    const resultNameIntro=document.querySelector('.resultIntro');
    resultNameIntro.innerHTML=infoList[point].nameIntro;

    const resultName=document.querySelector('.resultName');
    resultName.innerHTML=infoList[point].name;

    //사진 

    var resultImg = document.createElement('img');
    const imgDiv = document.querySelector("#resultImg");
    var imgURL = 'img/image-' + point + '.png';

    resultImg.src = imgURL;
    resultImg.alt = point;
    resultImg.classList.add('img-fluid');
    imgDiv.appendChild(resultImg);

    //디스크립션 
    
    const resultDesc1 = document.querySelector('.resultDesc1');
    const resultDescTitle1 = document.querySelector('.resultDescTitle1');

    resultDescTitle1.innerHTML = infoList[point].descTitle1;
    resultDesc1.innerHTML = infoList[point].desc1;
  
    const resultDesc2 = document.querySelector('.resultDesc2');
    const resultDescTitle2 = document.querySelector('.resultDescTitle2');
    resultDescTitle2.innerHTML = infoList[point].descTitle2;
    resultDesc2.innerHTML = infoList[point].desc2
}

function goResult(){ //결과창
    qna.style.WebkitAnimaiton="fadeOut 1s";
    qna.style.animation="fadeOut 1s"; //qna 사라져요 
    setTimeout(()=>{    
        result.style.webkitAnimaiton="fadeIn 1s"; //result 나타나요  
        qna.style.animation="fadeIn 1s";
        setTimeout(()=>{
         qna.style.display="none";
         result.style.display="block";
         },450);
    },450);

    setResult();

}

function goNext(qIdx){
    if(qIdx==endPoint){
        goResult(); //endpoint에 도달하면 결과창으로 이동
        return; 
    }
    var q=document.querySelector(".qBox");
    //q.innerHTML=qnaList[0].q 출력됨
    q.innerHTML=qnaList[qIdx].q;
    //변수 도입, gonext끝나고 또 호출.

    for(let i in qnaList[qIdx].a)
    {//질문을 더하는 함수 
        addAnswer(qnaList[qIdx].a[i].answer,qIdx);
    }

    //n/10
    var countStatusNum=document.querySelector('.countStatus');
    countStatusNum.innerHTML=(qIdx+1)+"/"+endPoint;

// 위에 바 
    var status=document.querySelector('.statusBar');
    status.style.width=(100/endPoint)*(qIdx+1)+"%"
}

function start(){ //onclick ->함수 실행
    main.style.WebkitAnimaiton="fadeOut 1s";
    main.style.animation="fadeOut 1s"; //메인은 사라져요 
    setTimeout(()=>{    
        qna.style.webkitAnimaiton="fadeIn 1s"; //qna 나타나요  
        qna.style.animation="fadeIn 1s";
        setTimeout(()=>{
         main.style.display="none";
         qna.style.display="block";
        },450);
        let qIdx=0;
        goNext(qIdx);

    },450);


}

