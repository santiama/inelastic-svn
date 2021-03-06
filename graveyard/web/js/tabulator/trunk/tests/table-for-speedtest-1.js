// a table example

function add_headcell( descriptor, headrow, descriptors )
{
  id = descriptor.id;
  text = descriptor.text;
  
  cell = $( '<td id="' + id + '">' + text + '</td>' );
  headrow.append( cell );
  descriptors[ id ] = descriptor;
}

function make_table_head( thetable ) {

  var shipping_choices =  {
  0: 'na',
  1: "1 Hour",
  2: "12 Hours",
  3: "24 Hours",
  4: "2 days",
  5: "1 week"
  };

  thead = $(thetable.children( 'thead' )[0]);
  headrow = $(thead.children( 'tr' )[0]);
  
  descriptors = {
    'sales_col': { text: 'Sales', datatype: 'upanddown' }, 
    'title_col': { text: 'Title', datatype: 'text' }, 
    'author_col': { text: 'Author', datatype: 'text' }, 
    'price_col': { text: 'Price', datatype: 'money' }, 
    'in_store_col': { text: 'In Store', datatype: 'boolean' },
    'shipping_col': { text: 'Shipping', datatype: 'single_choice', choices: shipping_choices },
    'bestseller_col': { text: 'Bestseller', datatype: 'single_choice_in_one_column' }, 
    'date_col': { text: 'Date of Publication', datatype: 'date', valid_range: [ '01/01/1970', '01/01/2010' ] }
  }

  establish_headrow_from_column_descriptors( headrow, descriptors );
  thetable.table_setcolumndescriptors( descriptors );

}


function add_headcell( id, text, headrow )
{
  cell = $( '<td id="' + id + '">' + text + '</td>' );
  headrow.append( cell );
}


function establish_headrow_from_column_descriptors( headrow, descriptors )
{
  for (var colid in descriptors) {
    descriptor = descriptors[ colid ];
    add_headcell( colid, descriptor.text, headrow );
  }
}


function make_table_skeleton( ) {
  
  table = $( '<table border="1"></table>' );
  
  thead = $( '<thead></thead' );
  table.append(thead);
  
  headrow = $( '<tr></tr>' );
  thead.append( headrow );

  tbody = $( '<tbody></tbody>' );
  table.append( tbody );
  
  return table;
}


function make_form() {
  return $( '<form> </form>' );
}


function make_test_table( div ) {

  // make the table skeleton
  thetable = make_table_skeleton();

  form = make_form();
  form.append( thetable );

  // add table skeleton to div
  div.append( form );

  // table contents
  make_table_head( thetable );

  var N = 50;
  var BestSeller = Math.floor( Math.random() * N );

  for (var i = 0; i < N; i++ ) {
    
    var sales = Math.floor( Math.random() * 100 ) - Math.floor(100/2);
    var price = Math.floor( Math.random() * 3000 ) / 100.;
    var shipping = Math.floor( Math.random() * 6 );
    var title = randSentence( 3, 10 );
    var author = randSentence( 2, 8 );
    var instore = Math.floor( Math.random() * 2 );
    thetable.table_appendrow_dataonly
      ( i, [sales, title, author, price, instore, shipping, i==BestSeller] );
    ;
  }

}


function randSentence(  maxnumberofwords, maxnumberofcharactersperword )
{
  var words = randWords(  maxnumberofwords, maxnumberofcharactersperword );

  var sentence = "";

  for ( var i=0; i<words.length; i++ ) {
    sentence += words[i];
    if (i<words.length-1) sentence += ' ';
  }
  
  return sentence;
}


function randWords( maxnumberofwords, maxnumberofcharactersperword )
{
  var nword = Math.floor( Math.random() * (maxnumberofwords-1) ) + 1;
  var words = [];

  for (var i=0; i<nword; i++) {
    words.push( randWord( maxnumberofcharactersperword ) );
  }
  
  return words;
}


function randWord( maxlength ) {
  var characters = "0123456789"
    + "ABCDEFGHIJKLMNOPQRSTUVWXTZ"
    + "abcdefghiklmnopqrstuvwxyz";
  
  var length = Math.floor( Math.random() * (maxlength-1) ) + 1;

  var word="";

  for (var j=0;j<length;j++) {
    var rand = Math.floor(Math.random() * characters.length);
    word += characters.substring(rand,rand+1);
  }

  return word;
}
