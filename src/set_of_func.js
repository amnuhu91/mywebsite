export const truncate_text = (str, strt,end) => {
    return str.length > end ? str.substring(strt, end) + "..." : str;
  };