import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/'
})

export const scrapeSite = (url: string) => {
  return api.post('/scrape/', { url })
}
