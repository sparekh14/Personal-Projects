// WebApplication - a class to used to configure the HTTP pipeline, and routes
// CreateBuilder() - initializes and instance of the WebApplicationBuilder class which is a builder for web applications and services
// builder - an instance of WebApplicatiionBuilder
var builder = WebApplication.CreateBuilder(args);


// Add services to the container.
builder.Services.AddControllersWithViews();

// Build() - method of the WebApplicationBuilder class that builds the web application with default configuration
// app - a configured WebApplication
var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

// runs the application
app.Run();
