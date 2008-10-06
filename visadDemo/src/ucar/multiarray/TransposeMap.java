// $Id: TransposeMap.java,v 1.2 2002/05/29 20:32:41 steve Exp $
/*
 * Copyright 1997-2000 Unidata Program Center/University Corporation for
 * Atmospheric Research, P.O. Box 3000, Boulder, CO 80307,
 * support@unidata.ucar.edu.
 * 
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2.1 of the License, or (at
 * your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
 * General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation,
 * Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
 */
package ucar.multiarray;
import java.lang.reflect.Array;

/**
 * Use with MultiArrayProxy to transpose two dimensions.
 *
 * @see IndexMap
 * @see MultiArrayProxy
 *
 * @author $Author: steve $
 * @version $Revision: 1.2 $ $Date: 2002/05/29 20:32:41 $
 */
public class
TransposeMap
		extends ConcreteIndexMap
{
	/**
	 * Create an IndexMap which swaps two dimensions.
	 *
	 * @param aa specifies one of the dimensions to swap
	 * @param bb specifies the other dimension to swap
	 */
	public
	TransposeMap(int aa, int bb)
	{
		init(new IMap(),
			new LengthsMap());
		aa_ = aa;
		bb_ = bb;
	}

	/**
	 * Create an IndexMap which swaps two dimensions.
	 *
	 * @param prev IndexMap to be composed with this.
	 * @param aa specifies one of the dimensions to swap
	 * @param bb specifies the other dimension to swap
	 */
	public
	TransposeMap(ConcreteIndexMap prev, int aa, int bb)
	{
		link(prev, new IMap(),
			new LengthsMap());
		aa_ = aa;
		bb_ = bb;
	}

	private class
	IMap extends ZZMap
	{
		public synchronized int
		get(int key)
		{
			if(key == aa_)
			{
				return super.get(bb_);
			}
			// else
			if(key == bb_)
			{
				return super.get(aa_);
			}
			// else
			return super.get(key);
			
		}
	}

	private class
	LengthsMap extends ZZMap
	{
		public int
		get(int key)
		{
			if(key == aa_)
				return super.get(bb_);
			// else
			if(key == bb_)
				return super.get(aa_);
			// else
			return super.get(key);
		}
	}

 /**/

	/* WORKAROUND: Inner class & blank final initialize compiler bug */
	private /* final */ int aa_;
	private /* final */ int bb_;

 /* Begin Test */
	public static void
	main(String[] args)
	{
		final int [] shape = {32, 48, 64};
		MultiArrayImpl delegate =
			new MultiArrayImpl(Integer.TYPE, shape);
		{
			final int size = MultiArrayImpl.numberOfElements(shape);
			for(int ii = 0; ii < size; ii++)
				java.lang.reflect.Array.setInt(delegate.storage,
					ii, ii);

		}
		IndexMap im = new TransposeMap(0, 2);
		MultiArray ma = new MultiArrayProxy(delegate, im);

		try {
			System.out.println("Rank  " + ma.getRank());
			int [] lengths = ma.getLengths();
			System.out.println("Shape { " + lengths[0] + ", "
					 + lengths[1] + ", "
					 + lengths[2] + " }");
			System.out.println(ma.getInt(new int[] {0, 0, 1}));
			System.out.println(ma.getInt(new int[] {0, 1, 0}));
			System.out.println(ma.getInt(new int[] {1, 0, 0}));
		}
		catch (java.io.IOException ee) {}
	}
 /* Test output java ucar.multiarray.TransposeMap
Rank  3
Shape { 64, 48, 32 }
3072
64
1
 /* End Test */
}
