from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Punctuation, Other


class VscStyle(Style):
    """
    A pygments style inspired by vsc.
    """
    background_color = "#1e1e1e"
    highlight_color  = "#264f78"
    default_style = ""
    styles = {
        Comment: "#6A9955",
        String: "#c3723b",
        Number: "#B5CEA8",
        Name: "#D4D4D4",
        Name.Decorator: "#DCDCAA",
        Name.Function: "#DCDCAA",
        Name.Class: "#DCDCAA",
        Name.Variable: "#9fb4c3",
        Name.Constant: "#9fb4c3",
        Keyword: "#569CD6",
        Generic: "#D4D4D4",
        Punctuation: "#D4D4D4",
        Operator: "#D4D4D4",
        Operator.Word: "#569CD6",
        Other: "#D4D4D4",
        Error: "#F44747",
        
        
    }