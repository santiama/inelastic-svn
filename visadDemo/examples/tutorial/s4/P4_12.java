/*
VisAD Tutorial
Copyright (C) 2000 Ugo Taddei
*/

package tutorial.s4;

// Import needed classes

import visad.*;
import visad.util.*;
import visad.java3d.DisplayImplJ3D;
import java.rmi.RemoteException;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

  /**
  VisAD Tutorial example 4_12
  Use ProjectionControl and its matrix
  Change aspect ratio
  We have the function rgbVal = h(RED, GREEN, BLUE)

  represented by the MathType
  ( (RED, GREEN, BLUE) -> rgbVal )
  Run program with "java P4_12"
 */



public class P4_12{

// Declare variables
  // The domain quantities longitude and latitude
  // and the dependent quantity rgbVal

  private RealType red, green, blue;
  private RealType rgbVal;

  // Tuple to pack longitude and latitude together

  private RealTupleType domain_tuple;


  // The function (domain_tuple -> rgbVal )

  private FunctionType func_domain_rgbVal;


   // Our Data values for the domain are represented by the Set

  private Set domain_set;


  // The Data class FlatField

  private FlatField vals_ff;

  // The DataReference from data to display

  private DataReferenceImpl data_ref;

  // The 2D display, and its the maps

  private DisplayImpl display;
  private ScalarMap redXMap, greenYMap, blueZMap;
  private ScalarMap redMap, greenMap, blueMap;
  private ScalarMap rgbMap;

  public P4_12(String []args)
    throws RemoteException, VisADException {

    // Create the quantities
    // Use RealType(String name, Unit unit, Set set);

    red = RealType.getRealType("RED", null, null);
    green = RealType.getRealType("GREEN", null, null);
    blue = RealType.getRealType("BLUE", null, null);

    domain_tuple = new RealTupleType(red, green, blue);

    // The independent variable

    rgbVal = RealType.getRealType("RGB_VALUE", null, null);

    // Create a FunctionType (domain_tuple -> range_tuple )
    // Use FunctionType(MathType domain, MathType range)

    func_domain_rgbVal = new FunctionType( domain_tuple, rgbVal);

    // Create the domain Set
    // Integer3DSet(MathType type, int lengthX, int lengthY, int lengthZ)

    int NCOLS = 32;
    int NROWS = 32;
    int NLEVS = 16;

    domain_set = new Linear3DSet(domain_tuple,  -Math.PI, 2.0*Math.PI, NROWS,
                                                -Math.PI, Math.PI, NCOLS,
                                                -Math.PI, 0.0,     NLEVS );

    // Our 'flat' array

    double[][] flat_samples = new double[1][NCOLS * NROWS * NLEVS];

    // Fill our 'flat' array with the rgbVal values
    // by looping over NCOLS and NROWS

    // but first get the Set samples to help with the calculations
    float[][] set_samples = domain_set.getSamples( true );

    // Note the use of an index variable, indicating the order of the samples


    int index = 0;

    for(int l = 0; l < NLEVS; l++)

      for(int c = 0; c < NCOLS; c++)

        for(int r = 0; r < NROWS; r++){

	      // set value for RealType rgbVal
	      flat_samples[0][ index ] =   (float) (Math.sin( 0.850 * (double)
	                                                  set_samples[0][ index ]) ) +

                                      (float) Math.exp( - 1.0/(Math.pow((double)
	                                     set_samples[1][ index ]*0.5/Math.PI, 2.0 ) -1.0 )) +

                                       (float) (Math.cos( 0.650 * (double)
	                                                  set_samples[2][ index ]) ) ;


	      // increment index
	      index++;

      }

    // Create a FlatField
    // Use FlatField(FunctionType type, Set domain_set)

    vals_ff = new FlatField( func_domain_rgbVal, domain_set);

    // ...and put the rgbVal values above into it

    // Note the argument false, meaning that the array won't be copied

    vals_ff.setSamples( flat_samples , false );

    // Create Display and its maps

    // This is new: a 3D display

    display = new DisplayImplJ3D("display1");

    // Get display's graphics mode control and draw scales

    GraphicsModeControl dispGMC = (GraphicsModeControl)  display.getGraphicsModeControl();
    dispGMC.setScaleEnable(true);
    dispGMC.setProjectionPolicy(DisplayImplJ3D.PARALLEL_PROJECTION);

    // Get the projection control
    ProjectionControl projCont = display.getProjectionControl();

    double[] aspect = new double[]{1,0.66,0.33};
    projCont.setAspect( aspect );

    // get projection matrix and print it out
    double[] projMatrix = projCont.getMatrix();
    for(int i = 0;i<16;i++)
      System.out.println(projMatrix[i]);

    // set new projection matrix
    double[] newMatrix = new double[]{1,0,0,0,
                                      0,1,0,0,
                                      0,0,1,0,
                                      0,0,0,1};
    // uncomment to set above matrix

    //projCont.setMatrix( newMatrix );


    // Create the ScalarMaps: latitude to XAxis, longitude to YAxis and
    // rgbVal to ZAxis and to RGB
    // Use ScalarMap(ScalarType scalar, DisplayRealType display_scalar)

    redXMap = new ScalarMap( red,    Display.XAxis );
    greenYMap = new ScalarMap( green, Display.YAxis );
    blueZMap = new ScalarMap( blue, Display.ZAxis );

    rgbMap= new ScalarMap( rgbVal,  Display.RGB );


    // Add maps to display

    display.addMap( redXMap );
    display.addMap( greenYMap );
    display.addMap( blueZMap );

    display.addMap( rgbMap);

    // Create a data reference and set the FlatField as our data

    data_ref = new DataReferenceImpl("data_ref");

    data_ref.setData( vals_ff );

    // Add reference to display

    display.addReference( data_ref );

    blueZMap.setRange(-Math.PI, Math.PI );

    // Create application window and add display to window

    JFrame jframe = new JFrame("VisAD Tutorial example 4_12");
    jframe.getContentPane().add(display.getComponent());


    // Set window size and make it visible

    jframe.setSize(300, 300);
    jframe.setVisible(true);


  }


  public static void main(String[] args)
    throws RemoteException, VisADException
  {
    new P4_12(args);
  }

} //end of Visad Tutorial Program 4_12