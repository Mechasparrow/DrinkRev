function get_rating() {
    let rating_elem = document.querySelector("#id_rating");
    return rating_elem;
}

function modify_rating(rating_num) {
    let rating_elem = get_rating();
    rating_elem.value = rating_num;
}

function get_rating_num() {
    let rating_elem = get_rating();
    console.log(rating_elem.value);
    return rating_elem.value;
}

function render_rating() {
    let num = parseInt(get_rating_num());
    let empty_drink_url = "/static/drinkreviews/emptydrink.png";
    let drink_url = "/static/drinkreviews/drink.png";

    let buckets = document.querySelectorAll(".rating-bucket");

    for (let i = 0; i < buckets.length; i++) {
        var bucket = buckets[i];
        if (i < num) {
            bucket.setAttribute("src", drink_url);
        }else {
            bucket.setAttribute("src", empty_drink_url);
        }
    }

    console.log(buckets);
}

function select_rating(num) {
    modify_rating(num);
    render_rating()
}

get_rating_num();