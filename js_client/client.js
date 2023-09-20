// const loginForm = document.getElementById('login-form')
// const baseEndpoint = "http://localhost:8000/api"
// if (loginForm){
//     loginForm.addEventListener('submit',handlelogin)

// }


// function handlelogin(event) {
//     console.log(event);
//     event.preventDefault()
//     const loginEndpoint = `${baseEndpoint}/token/`
//     let loginFormData = new FormData(loginForm)
//     let loginObjectData = Object.fromEntries(loginFormData)
//     console.log(loginObjectData);
//     let bodyStr = JSON.stringify(loginObjectData)
//     const options = {
//         "method":"POST",
//         headers : {
//             "Content-Type": "application/json"
//         },
//         body:bodyStr

//     }
//     fetch(loginEndpoint,options)
//     .then(response=>{
//         console.log(response);
//         return response.json()
//     })
//     .then(x => {
//         console.log(x);
//     })
//     .catch(err => {
//         console.log(('err',err));
//     })
// }

const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm) {
    // handle this login form
    loginForm.addEventListener('submit', handleLogin)
}
if (searchForm) {
    // handle this login form
    searchForm.addEventListener('submit', handleSearch)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options) //  Promise
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData,getProductList)
    })
    .catch(err=> {
        console.log('err', err)
    })
}

function handleSearch(event) {
    console.log(event)
    event.preventDefault()
    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const options = {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization":"Bearer tasdfs"
        }
    }
    fetch(endpoint, options) //  Promise
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(data => {
        writeToContainer(data)
    })
    .catch(err=> {
        console.log('err', err)
    })
}

function handleAuthData(authData,callback) {
    localStorage.setItem('access',authData.access)
    localStorage.setItem('refresh',authData.refresh)
    if (callback){
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data,null,4) + "</pre>"
    }
}

function getFetchOptions(method,body){
    return {
        method:method === null ? "GET" : method,
        headers: {
            "Content-Type":"application/json",
            "Authorization":`Bearer ${localStorage.getItem('access')}`
        },
        body : body ? body : null
    }

}

// function isTokenValid()

function getProductList() {
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()
    fetch(endpoint,options)
    .then(response=>{
        console.log(response);
        response.json()
    })
    .then(data => {
        console.log(data);
        writeToContainer(data)

    })

}
// getProductList()