function TaskDone(Boom)
{
  var bulletstyle= document.getElementById(Boom).style.textDecoration;

  if (bulletstyle == 'line-through')
  {
    document.getElementById(Boom).style.textDecoration='none';
  }
  else
  {
      document.getElementById(Boom).style.textDecoration='line-through';
  }
}

function Clear()
{
  var names = document.getElementsByClassName("task");
  for (var i = 0; i < names.length; i++)
  {
    names[i].style.textDecoration = 'none';
  }
}
