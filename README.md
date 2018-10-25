# Cluster
An interface-friendly and high-performance cluster analysis framework.

## Models[1-5]

| 类型              | 模型           | 稳定性 | 高维 | 大规模 | 适配数据  | 顺序敏感   | 异常敏感   |
| ----------------- | -------------- | ------ | ---- | ------ | --------- | ---------- | ---------- |
| partition         | K-means        | Middle | Yes  | no     | Convex    | Highly     | Highly     |
| partition         | K-medoids      | Low    | No   | No     | Convex    | Moderately | Little     |
| partition         | PAM            | Low    | No   | No     | Convex    | Moderately | Little     |
| partition         | CLARA          | High   | Yes  | No     | Convex    | Moderately | Little     |
| partition         | CLARANS        | Middle | Yes  | No     | Convex    | Highly     | Little     |
| partition         | AP             | Low    | No   | No     | Convex    | Moderately | Little     |
| hierarchy         | BIRCH          | High   | Yes  | No     | Convex    | Moderately | Little     |
| hierarchy         | CURE           | High   | Yes  | Yes    | Arbitrary | Moderately | Little     |
| hierarchy         | ROCK           | Middle | No   | Yes    | Arbitrary | Moderately | Little     |
| hierarchy         | Chameleon      | High   | No   | No     | Arbitrary | Moderately | Little     |
| fuzzyTheory       | FCM            | Middle | No   | No     | Convex    | Moderately | Highly     |
| fuzzyTheory       | FCS            | Low    | No   | No     | Arbitrary | Moderately | Highly     |
| fuzzyTheory       | MM             | Low    | No   | No     | Arbitrary | Moderately | Little     |
| distribution      | DBCLASD        | Middle | Yes  | Yes    | Arbitrary | Little     | Little     |
| distribution      | GMM            | High   | No   | No     | Arbitrary | Highly     | Little     |
| density           | DBSCAN         | Middle | Yes  | No     | Arbitrary | Moderately | Little     |
| density           | OPTICS         | Middle | Yes  | No     | Arbitrary | Little     | Little     |
| density           | Mean-shift     | Low    | No   | No     | Arbitrary | Little     | Little     |
| density           | DENCLUE        | Middle | Yes  | Yes    | Arbitrary | Moderately | Little     |
| graph             | CLICK          | High   | Yes  | No     | Arbitrary | Highly     | Highly     |
| graph             | MST            | High   | Yes  | No     | Arbitrary | Highly     | Highly     |
| graph/spectral    | SM             | Middle | No   | Yes    | Arbitrary | Little     | Little     |
| graph/spectral    | NJW            | Middle | No   | Yes    | Arbitrary | Little     | Little     |
| grid              | STING          | High   | Yes  | Yes    | Arbitrary | Little     | Little     |
| grid              | CLIQUE         | High   | No   | Yes    | Convex    | Little     | Moderately |
| grid              | Wavecluster    | High   | Yes  | No     | Arbitrary | Little     |            |
| fractalTheory     | FC             | High   | Yes  | Yes    | Arbitrary | Highly     | Little     |
| modelBased        | COBWEB         | Middle | Yes  | No     | Arbitrary | Little     | Moderately |
| modelBased        | GMM            | High   | No   | No     | Arbitrary | Highly     | *          |
| modelBased        | SOM            | Low    | No   | Yes    | Arbitrary | Little     | Little     |
| modelBased        | ART            | High   | Yes  | No     | Arbitrary | Highly     | Highly     |
| kernel            | kernel K-means | Middle | No   | No     | Arbitrary | Moderately | Little     |
| kernel            | kernel SOM     | High   | No   | No     | Arbitrary | Little     | Little     |
| kernel            | kernel FCM     | Middle | No   | No     | Arbitrary | Moderately | Little     |
| kernel            | SVC            | Low    | No   | No     | Arbitrary | Little     | Little     |
| kernel            | MMC            | Low    | No   | No     | Arbitrary | Little     | Little     |
| kernel            | MKC            | Low    | No   | No     | Arbitrary | Little     | Little     |
| swarmIntelligence | ACO_based (LF) | Low    | No   | No     | Arbitrary | Little     | Highly     |
| swarmIntelligence | PSO_based      | Low    | No   | No     | Arbitrary | Moderately | moderately |
| swarmIntelligence | SFLA_based     | Low    | No   | No     | Arbitrary | Moderately | moderately |
| swarmIntelligence | ABC_based      | Low    | No   | No     | Arbitrary | Moderately | moderately |
| quantumTheory     | QC             | Middle | No   | No     | Convex    | Little     | Little     |
| quantumTheory     | DQC            | Middle | No   | No     | Convex    | Little     | Little     |
| Spectral          | SM             | Middle | No   | Yes    | Arbitrary | Little     | Little     |
| Spectral          | NJW            | Middle | No   | Yes    | Arbitrary | Little     | Little     |
| stream            | singlePass     |        |      |        |           |            |            |
| stream            | STREAM         | Middle | Yes  | No     | Convex    | Highly     | Highly     |
| stream            | CluStream      | High   | Yes  | No     | Convex    | Highly     | Highly     |
| stream            | HPStream       | High   | Yes  | Yes    | Convex    | Highly     | Highly     |
| stream            | DenStream      | High   | Yes  | No     | Arbitrary | Highly     | Little     |

## Reference

[[1] A comprehensive Survey of Clustering Algorithms, Rui Xu, 2015]()

[[2] Survey of Clustering Algorithms, Rui Xu, 2005]()

[[3] Data clustering: a review, AK jain, ACM computing surveys (CSUR), 1999](https://dl.acm.org/citation.cfm?id=331504)

[[4] Mining data streams: a review, MM Gaber, A Zaslavsky, S Krishnaswamy - ACM Sigmod Record, 2005](https://dl.acm.org/citation.cfm?id=1083789)

[[5] Subspace clustering for high dimensional data: a review, L Parsons, E Haque, H Liu- Acm Sigkdd Explorations Newsletter, 2004](https://dl.acm.org/citation.cfm?id=1007731)

[[6] Large-scale cluster management at Google with Borg, A Verma - Proceedings of the …, 2015](https://dl.acm.org/citation.cfm?id=2741964)

