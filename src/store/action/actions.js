    import * as actionTypes from "./actionTypes"
import axios from "axios"
import {SERVER_PORT} from "../config"
import setAuthToken from "../../utils/setAuthToken"
import jwt_decode from "jwt-decode";


export const getBrandData = dispatch => (setOptionFlag) => {
    

    axios
    .get(`${SERVER_PORT}/apis/product/carbrand/`)
    .then( res => {
        if (setOptionFlag) {
            setOptionFlag(false)
        }
        res.status === 200
        ? dispatch({type: actionTypes.GET_BRAND_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err => {
        if (setOptionFlag) {
            setOptionFlag(false)
        }
        console.log(err)
    });

}
export const getModelData = dispatch => (brand_id, setPageFlag) => {
    axios
    .get(`${SERVER_PORT}/apis/product/carmodel/?brand_id=${brand_id}`)
    .then( res => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        
        res.status === 200
        ? dispatch({type: actionTypes.GET_MODEL_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        console.log(err)
    });
    
}
export const getEngineData = dispatch => (model_id, setPageFlag) => {
    axios
    .get(`${SERVER_PORT}/apis/product/engine/?model_id=${model_id}`)
    .then( res => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        res.status === 200
        ? dispatch({type: actionTypes.GET_ENGINE_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err =>{
        if (setPageFlag) {
            setPageFlag(false)
        }
         console.log(err)
     });
    
}
export const getCategoryData = dispatch => async (setOptionFlag) => {
    await axios
    .get(`${SERVER_PORT}/apis/blog/category/`)
    .then( res => {
        setOptionFlag(false)
        res.status === 200
        ? dispatch({type: actionTypes.GET_CATEGORY_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err => {
        setOptionFlag(false)
        console.log(err)
    });
}
export const getPostData = dispatch => (setPageFlag) => {
    
    axios
    .get(`${SERVER_PORT}/apis/blog/post/`)
    .then( res => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        res.status === 200
        ? dispatch({type: actionTypes.GET_POST_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        console.log(err)
    });
}
export const getSubmissionData = dispatch => async (setPageFlag) => {
    

    await axios
    .get(`${SERVER_PORT}/apis/submission/submission/`)
    .then( res => { 
        if (setPageFlag) {
            setPageFlag(false)
        }
        res.status === 200
        ? dispatch({type: actionTypes.GET_SUBMISSION_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        console.log(err)
    });

}
export const getFAQData = dispatch => async (setPageFlag) => {
    

    await axios
    .get(`${SERVER_PORT}/apis/software/faq/`)
    .then( res => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        res.status === 200
        ? dispatch({type: actionTypes.GET_FAQ_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err => {
        if (setPageFlag) {
            setPageFlag(false)
        }
        console.log(err)
    });

}
export const getDownloadSoftware = dispatch => async (setPageFlag) => {
    await axios
    .get(`${SERVER_PORT}/apis/software/downloadable-software/`)
    .then( res => { 
        if (setPageFlag) {
            setPageFlag(false)
        }
        res.status === 200
        ? dispatch({type: actionTypes.GET_DS_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err =>{
        if (setPageFlag) {
            setPageFlag(false)
        }
        console.log(err)
    });
}
export const getYoutube = dispatch => () => {
    axios
    .get(`${SERVER_PORT}/apis/software/youtube/`)
    .then(res=>{
        res.status === 200
        ? dispatch({type: actionTypes.GET_YOUTUBE_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err=>{
        console.log(err)
    })
}
export const getTiktok = dispatch => () => {
    axios
    .get(`${SERVER_PORT}/apis/software/tiktok/`)
    .then(res=>{
        res.status === 200
        ? dispatch({type: actionTypes.GET_TIKTOK_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err=>{
        console.log(err)
    })
}
export const getTeamCarousel = dispatch => () => {
    axios
    .get(`${SERVER_PORT}/apis/software/teamcarousel/`)
    .then(res=>{
        res.status === 200
        ? dispatch({type: actionTypes.GET_TEAMCAROUSEL_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err=>{
        console.log(err)
    })
}
export const getTopCarousel = dispatch => () => {
    axios
    .get(`${SERVER_PORT}/apis/software/top-carousel/`)
    .then(res=>{
        res.status === 200
        ? dispatch({type: actionTypes.GET_TOPCAROUSEL_DATA, pagedatas:res.data})
        : Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
    })
    .catch(err=>{
        console.log(err)
    })
}
export const submitSubmission = dispatch => async (postData, setAlert, errVal) => {
        await axios
        .post(`${SERVER_PORT}/apis/submission/submission/`, postData)
        .then(res=>{
            if (res.status === 201) {

                dispatch({type: actionTypes.ADD_SUBMISSION_DATA, pagedatas:res.data})
                if (setAlert && errVal) {
                    setAlert({
                        flag: "success",
                        val: errVal.success1 
                    })
                }
                
            } else {
                if (setAlert && errVal) {
                    setAlert({
                        flag: "failed",
                      val: errVal.error1 
                    })
                }
                Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
            }
        })
        .catch(err => {
            if (setAlert && errVal) {
                    setAlert({
                        flag: "failed",
                      val: errVal.error2 
                    })
                }
            console.log(err)
        })
}
export const submitBlog = dispatch => async (postData, setAlert, errVal) => {

        await axios
        .post(`${SERVER_PORT}/apis/blog/post/`, postData)
        .then(res=>{
            if (res.status === 201) {
                
                dispatch({type: actionTypes.ADD_POST_DATA, pagedatas:res.data})
                setAlert({
                  flag: "success",
                  val: errVal.success1
                })
            } else {
                setAlert({
                  flag: "failed",
                  val: errVal.error1
                })
                Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
            }
        })
        .catch(err => {
            setAlert({
                flag: "failed",
                val: errVal.error2
            })
            console.log(err)
        })
}
export const signupUser = dispatch => async (postData, setAlert, setSignupErrors, errVal, lang) => {
    let langVal
    if (lang === "en") {
        langVal = "/en"
    } else {
        langVal = ""
    }

        await axios
        .post(`${SERVER_PORT}${langVal}/rest-auth/registration/`, postData)
        .then(res=>{
            if (res.status === 201) {
                setAlert({
                    flag: "success",
                    val: errVal.success2
                })
            } else {
                setAlert({
                    flag: "failed",
                    val: errVal.error1
                })
                Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
            }
        })
        .catch(err=>{
            if (err.response.data.password1 && err.response.data.password1.length > 0) {
                setSignupErrors({
                    password1: err.response.data.password1
                })
            } else {
                setAlert({
                    flag: "failed",
                    val: errVal.error2
                })
            }          
        })

}
export const setCurrentUser = decoded=> {
    return {
        type: actionTypes.SET_CURRENT_USER,
        payload: decoded
    }
}
export const loginUser = dispatch => async (loginData, setAlert, setLoginErrors, lang, errVal, history, visit_url) => {
    let langVal
    if (lang === "en") {
        langVal = "/en"
    } else {
        langVal = ""
    }
    let visitUrl
    if (visit_url) {
        visitUrl = visit_url
    } else {
        visitUrl = "/"
    }

        await axios
        .post(`${SERVER_PORT}${langVal}/rest-auth/login/`, loginData)
        .then(res=>{
            if (res.status === 200) {
                setAlert({
                    flag: "success",
                    val: `${errVal.success1} ${res.data.user.username}`
                })
                let token
                if (res.data.token) {
                    token = res.data.token
                } else if (res.data.key) {
                    token = res.data.key
                }
                localStorage.setItem("jwtToken", token)
                setAuthToken(token);
                const decoded = jwt_decode(token)
                dispatch(setCurrentUser(decoded))
                history.push(visitUrl)
            } else {
                setAlert({
                    flag: "failed",
                    val: errVal.error1
                })
                Promise.reject(`Can"t communicate with REST API server (${res.statusText})`)
            }
        })
        .catch(err=> {
            if (err.response.data.non_field_errors) {
                setLoginErrors({
                    email: err.response.data.non_field_errors
                })
            } else {
                setAlert({
                    flag: "failed",
                    val: errVal.error2
                })
            }
            console.log(err)
        })

}
export const changeLang = (val) => {
        return {
            type: actionTypes.CHANGE_LANG,
            payload: val
        }
}
export const saveVisitUrl = (url) => {
    return {
        type: actionTypes.VISITURL,
        payload: url
    }
}
export const logoutUser = () =>dispatch=> {
    axios
    .post(`${SERVER_PORT}/rest-auth/logout/`)
    .then(res => console.log(res))
    .catch(err => console.log(err))
    localStorage.removeItem("jwtToken");
    setAuthToken(false);
    setAuthToken(false);
    dispatch(setCurrentUser({}));
}
export const submitCacheSubmission = dispatch => (data) => {
    console.log("hahah", data)
    dispatch({
        type: actionTypes.SUBMIT_CACHE,
        payload: data
    })
}
// export const getVerifiedStatus = dispatch => async (user) => {

//     try {
//         console.log(user);
//         const userData = await axios.get( RestAPI.ORIGINAL_ENDPOINT + "general/users/verifiedstatus/" + user);     
//         return userData.data;
        
//     } catch (error) {
//         console.log(error.message);
//     }
// }