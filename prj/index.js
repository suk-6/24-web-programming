const key = require('./key.json');

const getWeather = () => {
    const dayString = getDate(new Date());
    const APIKEY = key.APIKEY;
    fetch(`https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0?serviceKey=${APIKEY}&base_date=${dayString}&base_time=0500&nx=64&ny=119&_type=json`).then(response => response.json()).then(data => {
        console.log(data)
        return data
    })
}

const getDate = (day) => {
    const year = day.getFullYear();
    const month = (day.getMonth() + 1).toString().padStart(2, '0');
    const date = day.getDate().toString().padStart(2, '0');

    return year + '-' + month + '-' + date;
}

getWeather()