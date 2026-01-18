# Istio Traffic Management Proof of Concept

This project is a focused **proof of concept** that demonstrates **Istio traffic management** using **DestinationRule** and **VirtualService** resources. The goal of this work was to understand how Istio controls service-to-service traffic **without changing application code or Kubernetes Services**.

Rather than building complex applications, the emphasis of this PoC is on **how traffic behavior can be defined declaratively at the service mesh layer**.

---

## What Was Done in This Project

In this project, we created **Istio DestinationRule and VirtualService configurations** for an existing microservice setup consisting of two services:

- **Auth service**
- **Payment service**

Both services were already deployed on Kubernetes. No changes were made to the application logic to manage traffic behavior.

---

## DestinationRule Configuration

DestinationRules were written to define **logical subsets** of services based on pod labels (for example, `version: v1` and `version: v2`). These subsets represent different versions of the same service.

The DestinationRule configurations also define **how traffic should be handled once it reaches a service**, such as load-balancing behavior and resilience settings. This allows Istio to understand the available service versions and manage traffic at the pod level.

---

## VirtualService Configuration

VirtualServices were created to define **how requests are routed to those subsets**. Using VirtualService rules, traffic was explicitly routed to specific service versions.

This enabled:
- Routing all traffic to a stable version (`v1`)
- Gradually introducing traffic to a newer version (`v2`) using weighted routing
- Applying routing logic without restarting pods or modifying deployments

VirtualService rules control **where traffic goes**, while DestinationRules define **what destinations exist**.

---

## Why This Matters

By writing only DestinationRule and VirtualService configurations, this PoC demonstrates that:

- Traffic behavior can be changed **independently of application code**
- Canary deployments can be controlled **purely through configuration**
- Load balancing and version selection are handled by the service mesh
- Changes take effect dynamically without redeploying services

This approach reflects how traffic management is handled in **real-world Istio-based production systems**.

---

## Summary

This proof of concept focuses exclusively on **Istio traffic routing** using DestinationRule and VirtualService resources. It shows how Istio can manage service versions, control traffic flow, and enable safe rollout strategies using declarative configuration alone.
