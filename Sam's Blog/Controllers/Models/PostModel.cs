namespace samarth_blog_app.Models;

public class PostModel
{
    public int Id {get; set;} // the post ID number

    public string Title {get; set;} // the post title

    public string Body {get; set;} // the content of the post

    public DateTime CreatedtAt {get; set;} // the time the post was created

    public DateTime UpdatedAt {get; set;} // the time the post was updated (default is set to CreatedAt)
}
