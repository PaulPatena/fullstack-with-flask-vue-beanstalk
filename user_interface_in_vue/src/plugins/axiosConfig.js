import axios from 'axios'

const instance = axios.create({
    // When running the UI debug server and backend debug server, connect to backend port 5000
    baseURL: `${location.protocol}//${location.hostname}:${process.env.VUE_APP_DEBUG_PORT ==='yes' ? '5000' : location.port}`
})

export default instance
