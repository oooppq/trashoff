let percent = 70;

let rank1 = "H";
let rank2 = "S";
let rank3 = "Y";
let rank4 = "E";
$(".univ_box").hide();
var result = {
    H: {
        color: "#011241",
        univ: "HONGIk",
        name: "HONGIK UNIVERSITY",
        img: "/static/trashcan_H.png",


    },
    E: {
        color: "#006E38",
        univ: "EWHA",
        name: "EWHA UNIVERSITY",
        img: "/static/trashcan_E.png",


    },
    S: {
        color: "#AD0F0A",
        univ: "SOGANG",
        name: "SOGANG UNIVERSITY",
        img: "/static/trashcan_S.png",


    },
    Y: {
        color: "#003876",
        name: "YONSEI UNIVERSITY", univ: "YONSEI",
        img: "/static/trashcan_Y.png",


    },


};

$(".r1_univ").html(result[rank1]["univ"]);
$(".r2_univ").html(result[rank2]["univ"]);
$(".r3_univ").html(result[rank3]["univ"]);
$(".r4_univ").html(result[rank4]["univ"]);


$(".r1").click(function () {
    $(".container").css("opacity", "50%");
    $(".univ_box").show();
    $(".univ_box").css("color", result[rank1]["color"]);
    $(".univ_title").html(result[rank1]["name"]);
    $(".univ_img").attr("src", result[rank1]["img"]);
    $(".percentage").html(percent + "%");
    $(".univ_box").click(function () {


        $(".univ_box").hide();
        $(".container").css("opacity", "100%");
    });



});
$(".r2").click(function () {
    $(".container").css("opacity", "50%");
    $(".univ_box").show();
    $(".univ_box").css("color", result[rank2]["color"]);
    $(".univ_title").html(result[rank2]["name"]);
    $(".univ_img").attr("src", result[rank2]["img"]);
    $(".percentage").html(percent + "%");
    $(".univ_box").click(function () {


        $(".univ_box").hide();
        $(".container").css("opacity", "100%");
    });



});

$(".r3").click(function () {
    $(".container").css("opacity", "50%");
    $(".univ_box").show();
    $(".univ_box").css("color", result[rank3]["color"]);
    $(".univ_title").html(result[rank3]["name"]);
    $(".univ_img").attr("src", result[rank3]["img"]);
    $(".percentage").html(percent + "%");
    $(".univ_box").click(function () {


        $(".univ_box").hide();
        $(".container").css("opacity", "100%");
    });



});
$(".r4").click(function () {
    $(".container").css("opacity", "50%");
    $(".univ_box").show();
    $(".univ_box").css("color", result[rank4]["color"]);
    $(".univ_title").html(result[rank4]["name"]);
    $(".univ_img").attr("src", result[rank4]["img"]);
    $(".percentage").html(percent + "%");
    $(".univ_box").click(function () {


        $(".univ_box").hide();
        $(".container").css("opacity", "100%");
    });



});