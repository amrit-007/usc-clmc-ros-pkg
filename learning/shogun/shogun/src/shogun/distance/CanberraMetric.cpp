/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * Written (W) 2006-2009 Christian Gehl
 * Copyright (C) 2006-2009 Fraunhofer Institute FIRST
 */

#include <shogun/lib/config.h>
#include <shogun/lib/common.h>
#include <shogun/io/SGIO.h>
#include <shogun/distance/CanberraMetric.h>
#include <shogun/features/Features.h>
#include <shogun/features/SimpleFeatures.h>

using namespace shogun;

CCanberraMetric::CCanberraMetric()
: CSimpleDistance<float64_t>()
{
}

CCanberraMetric::CCanberraMetric(CSimpleFeatures<float64_t>* l, CSimpleFeatures<float64_t>* r)
: CSimpleDistance<float64_t>()
{
	init(l, r);
}

CCanberraMetric::~CCanberraMetric()
{
	cleanup();
}

bool CCanberraMetric::init(CFeatures* l, CFeatures* r)
{
	bool result=CSimpleDistance<float64_t>::init(l,r);

	return result;
}

void CCanberraMetric::cleanup()
{
}

float64_t CCanberraMetric::compute(int32_t idx_a, int32_t idx_b)
{

	int32_t alen, blen;
	bool afree, bfree;

	float64_t* avec=
		((CSimpleFeatures<float64_t>*) lhs)->get_feature_vector(idx_a, alen, afree);
	float64_t* bvec=
		((CSimpleFeatures<float64_t>*) rhs)->get_feature_vector(idx_b, blen, bfree);

	ASSERT(alen==blen);

	float64_t absTmp = 0;
	float64_t result=0;
	{
		for (int32_t i=0; i<alen; i++)
		{
			absTmp=fabs(avec[i])+fabs(bvec[i]);
			if(absTmp!=0)
				result+=fabs(avec[i]-fabs(bvec[i]))/absTmp;
		}

	}

	((CSimpleFeatures<float64_t>*) lhs)->free_feature_vector(avec, idx_a, afree);
	((CSimpleFeatures<float64_t>*) rhs)->free_feature_vector(bvec, idx_b, bfree);

	return result;
}
