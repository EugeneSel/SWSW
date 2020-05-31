insert into 
  test_schema.natural_disasters (
    title, 
    created_time, 
    description, 
    confidence
  )
values
  (
    'test_title', 
    curdate(), 
    'Well lets look at , what you wrote )) Seems like you re really a contused , mentally injured imbecile )) I can say this face to face ,how about you come and listen?) All this bullshit that you wrote is just plain simple fucking lies , you indoor rambo)) your life wouldn t get better cuz you wrote a lot)) bullshiting isn t a hard job, lots of fags like you melted in spring )) People say about fags like you: Mom didn t want it, dad didn t even try) Read my message to you closely and try to analise it and make some conclusions for yourself)', 
    77.8
  );

insert into 
  test_schema.tags (
    tag
  )
values
  (
    'Ukraine'
  );

insert into 
  test_schema.natural_disasters_have_tags (
    natural_disasters_id, 
    tag
  )
values
  (
    1, 
    'Ukraine'
  );