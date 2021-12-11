function search() {
    var search = document.getElementById("search").value;
    window.location.href = "{{ url_for('main.index') }}"+"?search="+search;
}