$$("tr")
  .filter((tr) => !tr.classList.contains("header"))
  .map((tr) => {
    const strings = [...tr.querySelectorAll("td")].map((td) => td.innerText);
    strings[1] = `"${strings[1]}"`;
    strings[3] = `"${strings[3]}"`;
    return strings.slice(1, 5).join(", ");
  })
  .join("\n");
