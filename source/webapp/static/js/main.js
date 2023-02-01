
    async function makeRequest(url, method='GET') {
        let response = await fetch(url, {method});
        if (response.ok) {
            return await response.json();
        } else {
            let error = new Error(response.statusText);
            error.response = response;
            throw error;
        }
    }

    async function buttonClick(event, ){
        let target = event.target;
        let data = await makeRequest(target.dataset.indexLink);
        let buttonLike = document.getElementById(`button${target.dataset.id}`);
        console.log(buttonLike);
        let plike = document.getElementById(`p${target.dataset.id}`);
        console.log(plike);
        plike.innerText = `likes: ${data.likes_amount}`;
        if(buttonLike.innerText === 'Like') {
            buttonLike.innerText = 'Unlike';
        } else {
            buttonLike.innerText = 'Like';
        }
    }

    async function onLoad(){
        let button = document.getElementById('button');
        if (button){
            button.onclick = buttonClick;
        }

    }

    window.addEventListener('load', onLoad)