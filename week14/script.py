#!/usr/bin/env python3

import matplotlib
matplotlib.use("Agg")

import scanpy.api as sc
sc.settings.autoshow = False

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

"""
sc.pp.filter_genes(adata, min_counts=1)  # only consider genes with more than 1 count
sc.pp.normalize_per_cell(                # normalize with total UMI count per cell
     adata, key_n_counts='n_counts_all')
filter_result = sc.pp.filter_genes_dispersion(  # select highly-variable genes
    adata.X, flavor='cell_ranger', n_top_genes=1000, log=True)
adata = adata[:, filter_result.gene_subset]     # subset the genes
sc.pp.normalize_per_cell(adata)          # renormalize after filtering
if log: sc.pp.log1p(adata)               # log transform: adata.X = log(adata.X + 1)
sc.pp.scale(adata)                       # scale to unit variance and shift to zero mean
"""

#sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
#sc.pl.pca(adata, save='nonfiltered')

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

#sc.tl.pca(adata, n_comps=50, zero_center=True, svd_solver='auto', random_state=0, return_info=False, use_highly_variable=None, dtype='float32', copy=False, chunked=False, chunk_size=None)
#sc.pl.pca(adata, save='filtered')

sc.pp.neighbors(adata, n_neighbors=15, n_pcs=None, use_rep=None, knn=True, random_state=0, method='umap', metric='euclidean', metric_kwds={}, copy=False)
sc.tl.louvain(adata, resolution=None, random_state=0, restrict_to=None, key_added=None, adjacency=None, flavor='vtraag', directed=True, use_weights=False, partition_type=None, partition_kwargs=None, copy=False)
sc.tl.tsne(adata, n_pcs=None, use_rep=None, perplexity=30, early_exaggeration=12, learning_rate=1000, random_state=0, use_fast_tsne=True, n_jobs=None, copy=False)
#sc.pl.tsne(adata, color = "louvain", save = ("tsne"))
#sc.pl.tsne(adata, color = ["louvain", "Tsc22d1", "Nrxn3"], save = ("Tsc22d1_tsne"))



#sc.tl.umap(adata, min_dist=0.5, spread=1.0, n_components=2, maxiter=None, alpha=1.0, gamma=1.0, negative_sample_rate=5, init_pos='spectral', random_state=0, a=None, b=None, copy=False)
#sc.pl.umap(adata, color = "louvain", save = ("umap"))

sc.tl.rank_genes_groups(adata, groupby = "louvain", use_raw=True, groups='all', reference='rest', n_genes=100, rankby_abs=False, key_added=None, copy=False, method='logreg', corr_method='benjamini-hochberg')
sc.pl.rank_genes_group_dotplot(adata, groupby="louvain", use_raw=None, log=False, num_categories=7, color_map='Reds', figsize=None, dendrogram=False, var_group_positions=None, var_group_labels=None, var_group_rotation=None, show=None, save="dotplot")
