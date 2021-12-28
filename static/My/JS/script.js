// console.log("krisha")

updatelike = (e) => {
    //     console.log("you clicked")
    //     console.log(e)
    //     console.log(e.dataset.id)
    //     console.log(e.dataset.color)
    let ID = e.dataset.id;
    let color = e.dataset.color;
    const url = "http://127.0.0.1:8000/liking";
    fetch(url, {
        method: "POST",
        headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken, },
        body: JSON.stringify({
            eventId: ID,
            is_liked: color
        })
    }).then((response) => {
        return response.json();
    })
        .then((data) => {
            // console.log('Data:', data)
            e.dataset.color = data.eventColor
            // console.log(e.className)
            if (data.eventColor)
                e.className = "fas fa-heart icon";
            else
                e.className = "far fa-heart icon"
        })
}