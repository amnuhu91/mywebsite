var truncate_text = function truncate_text(str, strt, end) {
    return str.length > end ? str.substring(strt, end) + "..." : str;
};